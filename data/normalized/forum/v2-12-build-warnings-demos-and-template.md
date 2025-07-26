# v2.12 Build warnings: Demos and Template

## Question

**Bil** asked on 05 May 2020

I updated to 2.12 a little while ago. First thing I did was open the demos solution, in VS 2019 16.6 preview 5. After fixing my local Nuget pointer to 2.12, I did a Nuget restore, then did a solution Build. 100s of warnings in the output window. Don't recall this when building previous version Demos project. Then created a new project using same VS version, and chose Telerik CRUD/Form/Chart template, Blazor server. That build is throwing the Async warnings I'm familiar with from the WeatherForecastService Error CS1998 about the lack of an awaits keyword. Is this something you mean to suppress in Editor.config? Same warnings thrown during build with VS 2019 16.5.4

## Answer

**Marin Bratanov** answered on 06 May 2020

Hi Bill, The "lack of awaits" warnings are not something we should suppress in our project template because it should be up to the developer to decide such settings, we should not hide warnings arbitrarily. Many of the relatively simple examples we provide so people can get started with as much copy-paste-run as possible showcase the ability to use async events, because that's what a real app uses, but they do not have actual async operations as that would make the examples very heavy and coupled, and they would not serve too well as
