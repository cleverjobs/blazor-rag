# Tabstrip Horizontal Scrollbar shows no matter what

## Question

**joh** asked on 05 May 2021

I have rearranged the row/col split in multiple ways. It seems no matter what I do the horizontal scrollbar always shows up. This only happens when the tabstrip has a "row/col" boostrap within it. If I don't put the row/col and just put a straight grid it properly doesn't not have a horizontal scrollbar. I even set the display initializer to wait until after the parameters have been set in the component. I tried the Kendo UI approach to force the tabstrip to not display the horizontal scrollbar, but I cannot seem to add an Id to the tabstrip. Horizontal Scrollbar Issue Grid Same Window Without Scrollbar html_code_example

## Answer

**Nadezhda Tacheva** answered on 07 May 2021

Hi John, When using Bootrap grid and setting up its row/col structure, the described behavior you are experiencing in terms of always visible scrollbar most likely stems from the default Bootrap setup of the "row" class. As it adds side margin, this results in the the container being wider than the parent and thus a scrollbar is always present. To solve this, you can add the following styles: <style>.row { margin-left: 0; margin-right: 0;
}
</style> Note: The above mentioned solution is based on a basic simulation of the code you are using (partly visible in the screenshot). You can find my reproduction attached along with the applied solution. For best results in terms of debugging on our side it will be better of you are able to send reproduction code instead of screenshot of the code. This could eliminate the possibility of missing some important context details while trying to reproduce the behavior you are experiencing. Another approach you may try is using the Blazor Form component for the Info tab. It allows you to generate a form based on your model, you can easily implement validation and customize the form as desired (including custom editors, additional buttons etc.). You can also organize the form elements in columns. With the simple syntax and the variety of features this component provides, it could save you multiple lines of code. I hope you will find the above information useful. If any further questions appear, please do not hesitate to contact us. Thank you for choosing Telerik UI for Blazor! Regards, Nadezhda Tacheva
