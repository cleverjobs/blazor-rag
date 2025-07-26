# How to code Blazor Server upload saveUrl with minimum web API?

## Question

**JayJay** asked on 03 Aug 2022

I'm trying to use the TelerikUpload control in a Blazor server project. I created a Blazor server project from the Telerik template. I'm trying to use only minimum web API for the upload endpoints. I haven't added controllers or routing to the configuration. The issue is that I'm getting a 400 error when I use the MapPost(). I've tried many different variations for the post action parameters. app.MapPost( "upload/save", async (IFormFile files)=>
{ if (files !=null )
{ var physicalPath=Path.Combine( "D:\\Source\\repos\\BlazorVPMS\\BlazorVPMS", "Upload/", files.FileName);
logger.Debug(physicalPath); using ( var fileStream=new FileStream(physicalPath, FileMode.Create))
{ await files.CopyToAsync(fileStream);
}
}
}); The only post method that works is this, after I added a form tag to the html. app.MapPost( "upload/save", async (IConfiguration config, HttpRequest request)=>
{ var files=request.Form.Files.First(); if (files !=null )
{ //string path=config["StoredFilesPath"]; var physicalPath=Path.Combine( "D:\\Source\\repos\\BlazorVPMS\\BlazorVPMS", "Upload/", files.FileName);
logger.Debug(physicalPath); using ( var fileStream=new FileStream(physicalPath, FileMode.Create))
{ await files.CopyToAsync(fileStream);
}
}
}); What do need to do to make this work with just using the IFormFile? Do I need to just add an API controller and routing to my configure and not use the minimum API?

### Response

**Dimo** commented on 08 Aug 2022

Jay, probably this SO thread will throw some light on the case.

### Response

**Jay** commented on 09 Aug 2022

Thank you, yes that StackOverflow thread helps. I finally added controllers to the project and have it working.
