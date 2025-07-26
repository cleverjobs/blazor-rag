# Blazor-coffe demo

## Question

**Ray** asked on 20 Jan 2022

Hi, I'm trying to run the blazor coffee demo on .NET 6 and VS2022. At first it fails to load and complains about not finding files related to blazor hot reload, and after turning off the hot reload feature the app starts but it can't find main.css and aspnetcore-browser-refresh.js? Is this not supported yet?

### Response

**Raymond** commented on 20 Jan 2022

I tried npm install in the client folder and dotnet build, but still I can't see main.css

### Response

**Raymond** commented on 20 Jan 2022

nevermind, the scss wasn't compiling, got it built now and it's working (haven't tried hot reload yet)

## Answer

**Joana** answered on 25 Jan 2022

Hi Raymond, I am glad that you were able to resolve the issue with the compilation. Indeed, there was an issue with the compilation of our themes. We changed the compilation and pushed the css in the app to facilitate the getting started experience. Thus, if you would like you could get the latest version of the app and test the app and the themes update. Regards, Joana
