# Run Blazor Demo

## Question

**Gen** asked on 26 Jan 2021

Downloaded source from Git. Was trying to run BlazingCoffee server version, got an error message for references: 1>------ Build started: Project: BlazingCoffee.Shared, Configuration: Debug Any CPU ------ Error occurred while restoring NuGet packages: Failed to retrieve information about 'Telerik.UI.for.Blazor.Trial' from remote source '[https://hexagonppm.pkgs.visualstudio.com/_packaging/d52ddb6c-0f38-494a-97a1-3133ffb82c9c/nuget/v3/flat2/telerik.ui.for.blazor.trial/index.json'.](https://hexagonppm.pkgs.visualstudio.com/_packaging/d52ddb6c-0f38-494a-97a1-3133ffb82c9c/nuget/v3/flat2/telerik.ui.for.blazor.trial/index.json'.) all referenced in project market with yellow triangle. VS 2019 v 16.8.4 What could be missing?

## Answer

**Marin Bratanov** answered on 27 Jan 2021

Hello Gennady, We have not yet released the 2.21.1 version, which is why it is not available. The automation updated the app as we are preparing the release so we can test it. To run it until 2.21.1 is live, just update the package reference to the currently available version - 2.21.0 Regards, Marin Bratanov
