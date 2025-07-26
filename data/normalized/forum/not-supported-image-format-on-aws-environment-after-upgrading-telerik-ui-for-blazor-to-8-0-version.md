# "Not supported image format." on AWS environment after upgrading Telerik UI for Blazor to 8.0 version

## Question

**n/an/a** asked on 28 Feb 2025

Currently I'm using below code that it throws an exception on AWS environment that "Not supported image format." using (var stream=Assembly.GetExecutingAssembly().GetManifestResourceStream($"ClaimForms.Server.Shared.Images.{logoFile}.png"))
{
ImageSource imageSource=new ImageSource(stream, ImageQuality.High);
CurrentEditor.DrawImage(imageSource, new Size(162, 42));
} Stream is not null and exception coming from ImageSource(). Could someone help me on this?

## Answer

**Vaibhav** answered on 03 Mar 2025

Hi , Before importing the document use the below code and get latest stable nuget package of Telerik.Documents.ImageUtils Telerik.Documents.ImageUtils.ImagePropertiesResolver defaultImagePropertiesResolver=new Telerik.Documents.ImageUtils.ImagePropertiesResolver(); Telerik.Windows.Documents.Extensibility.FixedExtensibilityManager.ImagePropertiesResolver=defaultImagePropertiesResolver; I am not sure this code solve your issue but you can try at least Thank you Vaibhav

### Response

**Dess | Tech Support Engineer, Principal** answered on 03 Mar 2025

Hello, I would recommend you to have a look at the following forum thread which seems to be related to this topic: [https://www.telerik.com/forums/telerik-windows-documents-fixed-exceptions-notsupportedimageformatexception-not-supported-image-format](https://www.telerik.com/forums/telerik-windows-documents-fixed-exceptions-notsupportedimageformatexception-not-supported-image-format) I hope you find this information helpful. Please, let me know if there is anything else I can assist you with. Regards, Dess | Tech Support Engineer, Principal

### Response

**n/a** commented on 03 Mar 2025

Hi Vaibhav and Dess. Thank you for your comment. Converting .png format to .jpg fixed my issue.
