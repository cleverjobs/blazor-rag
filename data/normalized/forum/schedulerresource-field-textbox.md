# SchedulerResource Field Textbox?

## Question

**Hyo** asked on 16 Sep 2020

Hi, I've been using the Kendo Scheduler for Blazor and have been following the examples from this doc: [https://docs.telerik.com/blazor-ui/components/scheduler/resources#one-resource](https://docs.telerik.com/blazor-ui/components/scheduler/resources#one-resource) However, the only examples for adding addition SchedulerResources are dropdownlists. Is there any way to add a Resource that's a textbox or any other input type? If I leave the Data attribute blank, an error is thrown. Thanks

## Answer

**Marin Bratanov** answered on 17 Sep 2020

Hello Hyong, The resources are a finite list of options defined by the developer, so the dropdown is the correct component to use as an editor. If you want to let the user input values that can then break the app, you can implement a custom edit form with the desired UX. Regards, Marin Bratanov

### Response

**Hyong** answered on 17 Sep 2020

Thank you! This is exactly what I was looking for
