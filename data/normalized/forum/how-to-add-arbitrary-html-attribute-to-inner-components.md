# How to add arbitrary HTML attribute to inner components?

## Question

**Seb** asked on 20 Jun 2023

Hi, one of my clients' automation team demands that each actionable element has it's own custom ID which they provide to us. So on our custom components (or any HTML element) we just add, eg: <div automation-id="some-important-div">...</div> However, when we consume Telerik Blazor UI components we're struggling to fullfill this requirement. Is there any way to add an arbitrary HTML attribute to inner components like this without having to re-implement each composable piece with our own template? We're fine with the look and feel of components, so it feels like an overkill to have to re-do everything (for example, the calendar's header with clickable date, arrows and "today" elements, and then the date cells for each view) just to add this ID without changing the styles or structure.

## Answer

**Stamo Gochev** answered on 26 Jun 2023

Hi Sebastian, Adding arbitrary HTML to the rendering of a Telerik Blazor component can yield unexpected results, e.g. the component might require certain elements to be at a specific position with a specific HTML. Adding other elements outside of the standard template parameters that are exposed can break the expected functionality of the component, so this is not something that we recommend. I see that you want to add an HTML attribute, which has less chance of interfering with the default functionality (seems like "data-automation-id" might be a better option compared to "automation-id" as "automation-id" is not a valid HTML attribute - HTML validators will report this as unexpected content). What I can suggest here (as the components intentionally do not allow this except for specific template and attribute parameters) is to use JavaScript and select the elements that you want to modify and update their rendering accordingly, e.g. the following can be used for the "Today" button of the Calendar: document.querySelector( ".k-calendar-nav-today" ).setAttribute( "data-automation-id", <some-id> ) Regards, Stamo Gochev
