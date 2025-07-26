# Telerik & Open Source Project

## Question

**Alb** asked on 09 Apr 2019

Hello, I have an open-source project in mind for which I want to use telerik blazor components for the UI part. Is it allowed to publish my project in github with references to kendo-blazor? now everyone will be able to download the kendo blazor nuget package but once it is GA what will happen? will you have some kind of license for open-source projects? Thanks.

## Answer

**Carl** answered on 09 Apr 2019

Hi Alberto! I'll answer your question based on the normal licensing that we have for our other UI components as that's probably the easiest model to look at from what we have today going in to any GA release of UI for Blazor. The way you can work with any of our UI components today inside of an open source project is by ensuring that you do not include the physical references (assemblies or any JS file) to Telerik UI for Blazor (or any of our other UI libraries). You can still include views that take advantage of UI for Blazor and sharing the actual code for how you interacted with our components is fine as well. However, for people to actually be able to run the project on their side, or also work with our UI components to contribute to this project, they would have to bring in our UI components themselves. This means that for a new user they should get access to UI for Blazor either in trial form or licensed form in order to contribute. It gets a little messy when looking in to production vs. non-production here, but generally the safest best is to have a license when doing this. What we've seen in the past is a notice in the README for the project that highlights that it uses UI for [X] and that in order to get up and running a dev looking in to the project should include their own reference to this product. Some include instructions of where to go to sign up for a trial and whatnots and then leave it up to the developer accessing the code to include the actual reference and NuGet package in the project on their side. I understand that the above might not be 100% ideal, but it has been successfully used in the past by OSS projects for some of our other UI libraries. Hopefully that helps clear some things up! Regards, -Carl Bergenhem PM, UI for Blazor
