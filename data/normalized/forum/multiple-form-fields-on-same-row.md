# Multiple Form Fields on same row

## Question

**Mar** asked on 22 Mar 2021

Hi. If I understand everything correctly, there is a one-to-one relationship between the <FormItem> element and model's data field. I am aware that I can use a <FormGroup> and set the columns attribute to indicate how many columns are needed. However, each <FormGroup> element renders a <fieldset> and <legend> element. Is it possible to place two, or more, data fields inside of one <FormItem>'s <Template> element? I'm looking for a way to not waste screen space by having each element of my form on it's own row. Using a <FormGroup> helps, however, I would like to avoid having all the extra <fieldset> and <legend> elements rendered. Thanks

## Answer

**Marin Bratanov** answered on 24 Mar 2021

Hi Marc, The FormItem is an item in the layout of the form that matches the columns and settings the form has. It it just a <div> element, no fieldsets or serious limitations here (but keep in mind we do have some CSS rules that might affect your content). You are free to add your own content and editors in it. If you want, you could add more than one textbox, for example. What you are looking for might be, however, better served by your own HTML layout inside a standard <EditForm> - you will have total freedom there to generate the layout, columns and design you want. Regards, Marin Bratanov
