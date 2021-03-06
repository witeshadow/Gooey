'''
Created on Jan 20, 2014

@author: Chris
'''
import wx


def _load_image(image_path):
  try:
    return wx.Bitmap(image_path)
  except:
    raise IOError('Invalid Image path')


def resize_bitmap(parent, _bitmap, target_height):
  '''
  Resizes a bitmap to a height of 89 pixels (the
  size of the top panel), while keeping aspect ratio
  in tact
  '''
  image = wx.ImageFromBitmap(_bitmap)
  _width, _height = image.GetSize()
  if _height < target_height:
    # print 'returning image without resizing'
    return wx.StaticBitmap(parent, -1, wx.BitmapFromImage(image))
  # print 'returning resized image'
  ratio = float(_width) / _height
  image = image.Scale(target_height * ratio, target_height,
                      wx.IMAGE_QUALITY_HIGH
  )
  return wx.StaticBitmap(parent, -1, wx.BitmapFromImage(image))


def _GetTargetSize(size):
  width, height = size
  aspect_ratio = float(width) / height
  tHeight = 79
  tWidth = int(tHeight * aspect_ratio)
  return (tWidth, tHeight)


if __name__ == '__main__':
  pass
