# Checkbox selection not working every time

## Question

**Nik** asked on 09 Oct 2019

Hello! In my example grids, the checkbox selection does not work every time. - If i click in a row directly on a checkbox, the checkbox is not checked - only on the second click - after the checkbox is onced checked, a new click directly changes the state instead of having a second required click - row clicks sometimes are not changing the checkbox state, sometimes they do It behaves very strange and not like on your demos pages. My grids are not having anything fancy (like jo, the GridCheckboxColumn and the SelectionMode) Anything that i can try to solve it? ... Niklas

## Answer

**Marin Bratanov** answered on 09 Oct 2019

Hello Niklas, Are you using a WASM project? If so, there is a known issue with checkboxes there: [https://feedback.telerik.com/blazor/1431737-grid-checkbox-not-checked-when-row-is-selected-client-side-blazor.](https://feedback.telerik.com/blazor/1431737-grid-checkbox-not-checked-when-row-is-selected-client-side-blazor.) If this is the issue you are experiencing, Vote and Follow the page for status updates. If not, please provide some more details on the problem - what version you're on, do you get errors, some sample markup (e.g., modify the examples from our docs), and perhaps a short video of what you get. Regards, Marin Bratanov

### Response

**Niklas** answered on 09 Oct 2019

Hey Marin, thank you very much for your fast feedback - yes, Client-Side Blazor application (because that's it what our future application requires). So, i'll remove the checkbox selection, i'm just testing and evaluating anyway :) Niklas

### Response

**Marin Bratanov** answered on 09 Oct 2019

Just a heads up then, Niklas, the client-side flavor is expected in May 2020, at the moment it is not official and supported by MS, it is still in Preview. Regards, Marin Bratanov

### Response

**Steve** answered on 11 Oct 2021

Check to make sure that you don't have the data as a parameter, AND that you're setting the value in the component. That was what I was doing and couldn't figure out why the check box worked subsequent times, but never the first.
