# Use Telerik with Blazor REPL

## Question

**Lie** asked on 23 Feb 2021

Hi there, is there a chance to use Telerik.UI.for.Blazor with Blazor REPL? [https://blazorrepl.com](https://blazorrepl.com) It would save a lot of time to both, customers of Telerik and Telerik support, when we could easily share code snippets,

## Answer

**Marin Bratanov** answered on 23 Feb 2021

Hello Liero, We are hoping that will be possible, too, and we're investigating the implementation options for a Telerik blazor dojo. Right now REPL has the ability to use nuget.org for adding packages which is a solid first step, but our components, being a commercial package, need to be behind a private feed, so that would need some more functionality - like a custom nuget.config, for example, or other way to input credentials. Regards, Marin Bratanov
