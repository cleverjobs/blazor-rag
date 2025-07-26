# BlazingCoffee Demo

## Question

**TomTom** asked on 25 Jun 2021

I'm trying out Telerik for Blazor. Got the latest BlazingCoffee code from Github and a trial license but when I build I get the following error. File to import not found or unreadable: ./node_modules/@progress/kendo-theme-default/dist/all.scss I am stumped on what to do to resolve this. Thanks.

### Response

**Ed** commented on 27 Jun 2021

Even though we're not using JavaScript, we do use a Sass based theme here. Please try running 'npm install' before running the app to resolve the Sass dependency. If that doesn't resolve the issue, please post your operating system. Paths can be slightly different on Linux vs. Windows. Best regards, Ed

### Response

**Tom** commented on 28 Jun 2021

Thanks, that resolved it.
