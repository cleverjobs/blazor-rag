# Gird.razor in client project in Visual studio 2019

## Question

**hug** asked on 06 May 2020

Hi, I was testing the creation of a new project in visual Studio 2019, using the template : CRUD, form, chart - Client App. (Telerik UI for Blazor 2.12.0) All the solution creation is ok. After, i define the Client project as Startup project, to test it but after F5, when i want to check the page GRID.RAZOR, the datas are not loaded. The call to the WeatherForecast service sent the reponse as text/html instead of Json. I didn't "touch" any code and in the service, Http.GetFromJsonAsync is used. Can anyone help me to understand why then content-type is not fine ? Thanks

## Answer

**Marin Bratanov** answered on 06 May 2020

Hi, You must set the Server project as the startup project, not the Client project. That's how we generate the project by default and you do not need to alter anything in order to run it. WebAssembly apps that are hosted in an ASP.NET Core project must start the server project, the Client project boils down to a set of static files. Regards, Marin Bratanov
