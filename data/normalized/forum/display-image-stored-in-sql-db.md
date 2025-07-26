# display image stored in sql db

## Question

**EdEd** asked on 30 Mar 2020

Hi, Can someone share an example of how to get an image from a FileStream'ed table in sqlserver into a column on a grid? Thanks ... Ed

## Answer

**Marin Bratanov** answered on 30 Mar 2020

Hello Ed, I would personally do this by exposing a handler (controller) and point the image src attribute to it - I can build the src with razor syntax according to the model data inside the grid column template. Another option is to put the base64 string data for the image in the model, and render it as-is in the image tag, again through a template. The downside of that is that this will increase the model size many times - base64 representations of images are pretty large. A third option is to have the byte[] directly in the model and render it out through some logic of yours so it results in an image or base64 encoding. The downside of that is that serializing that to a WASM app will be harder than for a server app, and it would weigh down the template rendering which would make the UI slower. That's why I would personally go with a handler. Regards, Marin Bratanov

### Response

**Ed** answered on 01 Apr 2020

It took me a bit. But I got what I need. For anyone else who might be interested. Here's how to get an image stored in sql server direct to a row/column in the grid without having to save a file to disk. I stored the full image and display a thumbnail in the grid row. Hope it helps ... Ed <GridColumn Field="ThumbNail" Title="Image" Width="75px"> <Template> @{ var ctx=context as YourModel; <img src="@(ctx.Thumb)" /> } </Template> </GridColumn> public static string GetThumb(byte[] img) { Image image; using (MemoryStream ms=new MemoryStream(img)) { ms.Position=0; image=Image.FromStream(ms); } Image thumb=image.GetThumbnailImage(64, 64, ()=> false, IntPtr.Zero); ImageConverter ic=new ImageConverter(); byte[] thumbBytes=(byte[])ic.ConvertTo(thumb, typeof(byte[])); string img64=Convert.ToBase64String(thumbBytes); string urlData=string.Format("data:image/jpg;base64, {0}", img64); return urlData; }
