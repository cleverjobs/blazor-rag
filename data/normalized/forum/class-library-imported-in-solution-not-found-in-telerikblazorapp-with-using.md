# Class library imported in solution not found in TelerikBlazorApp with "Using"

## Question

**Rém** asked on 21 Oct 2021

Hello, I created a class library designed to communicate with a database on my local computer. I wanted to import this class library to my Telerik blazor project (The demo one with some modifications). I uploaded my class library in the solution but when I want to use it (using instruction) in a new Page, I get the error " CS0246 The type or namespace name 'DataAccessLib' could not be found (are you missing a using directive or an assembly reference?)". Isn't possible to import other class librairies not made with telerik into a telerik project ? Greetings Rémy Macherel

## Answer

**Marin Bratanov** answered on 23 Oct 2021

Hi Rémy, Our package does not limit in any other ways other packages or class libraries you can use and reference. My best guess at the moment is that the target framework does not match, for Blazor you generally need to target netstandard2.1 while the default project template for an RCL targets netstandard2.0. I can also suggest you get the desired integration running on a vanilla project, and then add the Telerik components to it either via our VS wizard, or manually. Regards, Marin Bratanov Progress Telerik
