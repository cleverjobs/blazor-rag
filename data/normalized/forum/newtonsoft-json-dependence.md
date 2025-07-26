# Newtonsoft.Json dependence

## Question

**IonIon** asked on 21 Jan 2021

Hi, After 2.21.0 update, I noticed there is still a dependency of Newtonsoft.Json package in Telerik.DataSource, increasing the application payload with> 600k. Since .Net 5 moved to System.Text.Json context, maybe that dependency could be eliminated. Thanks, Ion

## Answer

**Marin Bratanov** answered on 21 Jan 2021

Hi Ion, Thank you for noticing this. It is a remnant that should not be used, in the last year we've been using the System.Text.Json serializer that comes with the framework and we've simply missed the packagereference to newtonsoft. If your app does not use newtonsoft, the linker should remove it for a wasm app, and for a server app it should not be too much of a problem. That said, I've logged a task for it to be removed. Regards, Marin Bratanov

### Response

**Ion** answered on 21 Jan 2021

Hi Marin, Of course, that dependency is not a real problem, so we will wait to be eliminated in the next version(s). Thanks, Ion

### Response

**Claudio** answered on 16 Apr 2021

I use Telerik.UI.For,Blazor 2.23.0 and found that Telerik.DataSource still depend on Newtonsoft.Json 12.0.2 This is a issue for us because when build the asp.net core server project, this library is copied on server bin, but the server project depend on a newer version of the same library and it produce a dependency version issue. How to avoid the reference of Newtonsoft.Json 12.0.2? Thanks

### Response

**Marin Bratanov** answered on 16 Apr 2021

Hello Claudio, Our next release (2.24.0) will not have the newtonsoft.json dependency. It is scheduled for mid-May. If this is urgent for you, in the meantime you can try a bindingRedirect to see if that can help with the assembly references, articles like this one, this one and this one can be starting points for that. Regards, Marin Bratanov
