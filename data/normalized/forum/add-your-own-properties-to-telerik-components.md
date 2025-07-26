# Add your own properties to Telerik Components

## Question

**Boh** asked on 17 Dec 2024

Hi, I couldn't find any articles about customizing Telerik components with additional properties, but want to add my own property directly to a Telerik component, like this: <TelerikWindow MyOwnProperty="SomeValue" /> I would like to avoid creating a custom wrapper component where I would use the Telerik component inside. Is there any way to achieve this directly with Telerik components without having to wrap them? Huge thanks for your response, Bohdan

## Answer

**Tsvetomir** answered on 18 Dec 2024

Hello Bohdan, Adding arbitrary HTML to the rendering of a Telerik Blazor component can yield unexpected results, e.g. the component might require certain elements to be at a specific position with a specific HTML. Adding other elements outside of the standard template parameters that are exposed can break the expected functionality of the component, so this is not something that we recommend. With that being said, I can inform you that we don't support such attributes declaratively. If this requirement is a must in your project, the alternative is to add a custom attribute with JSInterop. Just keep in mind the above-mentioned concerns. I hope you find well the provided information. Regards, Tsvetomir Progress Telerik
