# Blazor dojo

## Question

**Pet** asked on 04 May 2019

Hi, The Kendo UI dojo is great to extract some specific problems for the telerik support and for the solution. Can you make a dojo site for your blazor components? Best regards, Peter

## Answer

**Marin Bratanov** answered on 06 May 2019

Hi Peter, Thank you for your interest. Indeed, the Kendo Dojo is a great tool and I will discuss a Blazor dojo with the team. As things stand, I am not sure whether it is feasible, because it will require a lot of infrastructure for the builds, as well as running the code on our server, which is a serious security risk, while the Kendo dojo is basically some text that gets executed in an iframe inside the client browser only. What I can suggest on isolating issues at the moment is that creating a new Blazor project is quick, and the project is very small after a Clean operation, so it is easy to zip and send in a support ticket. Putting a problematic piece of code in a separate project will also isolate it from the potential issues in the main project, and it is often something in the business logic that causes a certain behavior, so the act of creating this sample can help you narrow down the problem and solve it without having to wait for a response. Regards, Marin Bratanov

### Response

**Peter** answered on 06 May 2019

Hi Marin, thank you, possible you know [https://blazorfiddle.com/](https://blazorfiddle.com/) with source [https://github.com/BlazorComponents/BlazorFiddle.Blazor.](https://github.com/BlazorComponents/BlazorFiddle.Blazor.) You're right, the left code is running on the server. Regards, Peter

### Response

**Marin Bratanov** answered on 06 May 2019

Hi Peter, Thank you for sharing these links. We will keep them in mind when reviewing the concept and feasibility of such a tool. In the meantime, it seems that the blazorfiddle.com site offers a saving ability, for example: [https://blazorfiddle.com/s/vx3qxb21,](https://blazorfiddle.com/s/vx3qxb21,) so you could use that. Regards, Marin Bratanov

### Response

**Peter** answered on 06 May 2019

Hi Marin, [https://blazorfiddle.com](https://blazorfiddle.com) has not a reference to Telerik.Blazor.Components.Grid, so the needed line @using Telerik.Blazor.Components.Grid will result in an error: obj/Debug/netstandard2.0/Index.g.i.cs(22,11): error CS0246: The type or namespace name 'Telerik' could not be found (are you missing a using directive or an assembly reference?) [/BlazorFiddleProject/BlazorFiddleProject.csproj] Regards, Peter

### Response

**Marin Bratanov** answered on 06 May 2019

You are right, of course, Peter. I don't know how I missed that. --Marin

### Response

**Peter** answered on 29 Nov 2020

Hi Marin, Are there any plans now that Telerik/Progress create a Blazor Dojo Server with references to the net 5 Telerik Controls? Regards, Peter

### Response

**Marin Bratanov** answered on 30 Nov 2020

Hello Peter, When technology for such a thing becomes available, we will consider it. At the moment, there is no similar technology that can also use custom nuget packages/feeds. Regards, Marin Bratanov
