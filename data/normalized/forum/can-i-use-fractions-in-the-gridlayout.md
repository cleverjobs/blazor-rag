# Can I use fractions in the GridLayout?

## Question

**Mar** asked on 02 Sep 2021

#app { height: 100 vh; /* grid container settings */ display: grid; grid-template-columns: 1 fr; grid-template-rows: auto 1 fr auto; grid-template-areas: 'header' 'main' 'footer'; } Can I use named areas and fractions?

## Answer

**Marin Bratanov** answered on 06 Sep 2021

Hello, The Width and Height parameters of the row and column respectively can take any suitable CSS unit, so that includes fractions. Setting the height in fractions is a bit more questionable as that usually requires some preset height on the container, as opposed to stretching it to the content, but you can add CSS to achieve that as well. The goal of the GridLayout component is to offer a quick and easy markup-based way for you to make a simple layout. It is especially suited to people migrating from non-web technology stacks (such as WPF, WinForms, Xamarin) to get their application layouts off the ground fast without having to ramp up with HTML and CSS knowledge. The goal of the GridLayout component is not to be a full replacement or wrapper over the standard CSS grid functionality, however. As such, it cannot expose all the possible options and settings in parameters. For really advanced use cases, I would recommend using the standard CSS approach and code. If we take the example you are using as base - it seems to be styling the entire app container, and as such it is possible only through CSS - a blazor component cannot render above the blazor app root element. Thus, for entire application layouts (in case you cannot put them in the blazor app so you could benefit from components like the splitter), using CSS is a perfectly valid and natural way to do this. Regards, Marin Bratanov

### Response

**Martin Herløv** commented on 07 Sep 2021

Thanks very good explanation. I think I stick with CSS Grid. Less structure code to look at.
