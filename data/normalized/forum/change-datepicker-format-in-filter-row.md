# Change DatePicker format in filter row

## Question

**Rob** asked on 17 Oct 2019

How can I change the datepicker format in filter row?

## Answer

**Marin Bratanov** answered on 18 Oct 2019

Hi Robert, I expect that the first feature to get implemented that will allow this is going to be filter templates: [https://feedback.telerik.com/blazor/1407773-custom-filter-components.](https://feedback.telerik.com/blazor/1407773-custom-filter-components.) So, I suggest you Follow it to get status notifications (I have added your Vote). Perhaps in a future version the grid markup will expose some filter configuration options, but it is too early to say when, how, and even if it will be available. Templating in Blazor is much more powerful than other places and it is likely that many things that in other suites are features sitting behind property flags will be implemented through templates in blazor. Regards, Marin Bratanov

### Response

**Graham** answered on 10 Dec 2020

Is there now a simple way of changing the date format in a filter row date field?

### Response

**Marin Bratanov** answered on 10 Dec 2020

Hello Graham, Filter templates are the way to do this, at least for the time being. Adding parameters is likely to result in a property hell type of situation - there is, at the moment, something like 10 different field types for editors (I think there may even be more if we count different numerical types), which means 10 properties just for that. That said, if you want a built-in feature for this, how would you expect it to be exposed? Regards, Marin Bratanov

### Response

**Graham** answered on 10 Dec 2020

I would be happy with a Filter Row template example for a date field column.

### Response

**Marin Bratanov** answered on 10 Dec 2020

Hi Graham, The documentation provides examples of using the filter row template: [https://docs.telerik.com/blazor-ui/components/grid/templates/filter.](https://docs.telerik.com/blazor-ui/components/grid/templates/filter.) You can find some in the demos too: [https://demos.telerik.com/blazor-ui/grid/custom-filter-row.](https://demos.telerik.com/blazor-ui/grid/custom-filter-row.) Are you facing a problem with adapting them to work with dates? Regards, Marin Bratanov

### Response

**Marin Bratanov** answered on 02 May 2021

Hi Robert, Graham, There is a new feature request for making this easier than using a filter template and you can Follow it here: [https://feedback.telerik.com/blazor/1517915-column-display-format-to-affect-the-filter-format-or-a-new-filter-format-parameter.](https://feedback.telerik.com/blazor/1517915-column-display-format-to-affect-the-filter-format-or-a-new-filter-format-parameter.) I've add both your votes to it. Regards, Marin Bratanov
