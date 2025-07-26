# Getting a 400 error on example

## Question

**Bit** asked on 21 May 2020

I'm working through this example, although slightly changed a bit, but I am getting a http 400. I am trying to upload a json file. The api path looks right when I debug but the request never makes it to the controller, however, I dont think its a routing issue as I would get a 404 error instead? [https://docs.telerik.com/blazor-ui/components/upload/overview](https://docs.telerik.com/blazor-ui/components/upload/overview)

## Answer

**BitShift** answered on 21 May 2020

Is this only for Client-side Blazor?

### Response

**BitShift** answered on 21 May 2020

Ok, figured out what I was missing. I thinkg I ran into this when I was building a Razorpages app. It was a routing issue after all. Got to enable routing to api and other controllers, in Startup This isnt enabled by default in a new Blazor server-side app (not sure about Client side) app.UseEndpoints(endpoints=> { endpoints.MapControllers(); endpoints.MapBlazorHub(); endpoints.MapFallbackToPage("/_Host"); });

### Response

**BitShift** answered on 21 May 2020

Oh, and its likely you will need to add this in Startup for ConfigureServices, if you havent already // web api services.AddControllers().AddNewtonsoftJson();

### Response

**Svetoslav Dimitrov** answered on 22 May 2020

Hello Randal, In our Create Project Wizard the endpoints.MapControllers(); should be enabled by default, you could try and create a new project and if it still missing you can open a Support ticket so we can further investigate. On the NewtonsoftJson framework, it is up to the application to define what third-party software products it will use. Regards, Svetoslav Dimitrov

### Response

**PH** answered on 31 May 2020

Hitting the same problem. Can you include an Upload page in the Telerik Blazor Server template, then we can see how it works?

### Response

**Svetoslav Dimitrov** answered on 01 Jun 2020

Hello Peter, You can see how to setup the Upload component from our documentation, link here: [https://docs.telerik.com/blazor-ui/components/upload/overview.](https://docs.telerik.com/blazor-ui/components/upload/overview.) In general, creating the Controller for the upload does not differ from the one you have for your database. You can also check our demos project that you have in the "demos" folder of your installation for an example. As attached file you can see a demo project which has the Upload set up. Regards, Svetoslav Dimitrov

### Response

**AFS331** commented on 12 Jan 2024

Thank you very much, this example solved my problem
