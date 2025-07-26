# Application has redirect to home page automatically after 25 minutes

## Question

**Mal** asked on 22 Jan 2024

Hello, I am developing a blazor application using telerik components and i am facing a problem, every 25 minutes during user operations, the application has refreshed and navigated to home page. Is there a parameter in blazor or telerik is affecting the behaviour. I need to avoid this action.

## Answer

**Nadezhda Tacheva** answered on 24 Jan 2024

Hi Malklin, No, the Telerik components cannot generally force the application to refresh and redirect - this is an application matter. You may test removing the Telerik components to see if you are observing the same behavior. I researched the matter for you and I found the following posts that may be useful: [https://stackoverflow.com/questions/74640312/blazor-web-site-keeps-reloading-randomly-every-few-seconds](https://stackoverflow.com/questions/74640312/blazor-web-site-keeps-reloading-randomly-every-few-seconds) [https://www.reddit.com/r/Blazor/comments/wiul5b/what_could_be_causing_my_blazor_server_app_to/](https://www.reddit.com/r/Blazor/comments/wiul5b/what_could_be_causing_my_blazor_server_app_to/) Regards, Nadezhda Tacheva Progress Telerik
