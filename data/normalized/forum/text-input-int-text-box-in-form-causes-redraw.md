# Text input int text box in form causes redraw

## Question

**Rob** asked on 18 Feb 2022

REPL How to avoid this?

## Answer

**Nadezhda Tacheva** answered on 23 Feb 2022

Hi Robert, It seems that the issue you are facing is associated with the new object() that you are setting to the form Model. The commonly used approach is to store the model instance in a field and pass that field to the Model parameter (you can check here for more details). With the following configuration, it looks like the problem is not reproducible: [https://blazorrepl.telerik.com/QcEQwRkt00pmtdyu43](https://blazorrepl.telerik.com/QcEQwRkt00pmtdyu43) I hope this will help you move forward with your application. Please let us know if any further questions appear. Regards, Nadezhda Tacheva Progress Telerik
