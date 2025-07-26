# Editor stay enabled in disabled FormItem

## Question

**Twa** asked on 25 Oct 2023

When I create a form with auto-generated fields and disable one of them (see code), the field indeed cannot be edited, but the associated spinner remains active (is a numeric field in this case), allowing the modification of the field's value. I believe that the underlying editor of the field (regardless of its type: datepicker, combobox, dropdownlist, numerictextbox or colorpicker) should be disabled when the FormItem is disabled, as it creates inconsistencies in the UI. <FormItems> <FormItem Field="@nameof(ViewModel.SomeField)" /> <FormItem Field="@nameof(ViewModel.NumericField)" Enabled="@some_variable" /> </FormItems> I understand that I could specify the template and disable the editor within it, but in this case, it would be necessary to define the templates of almost every FormItem, and the auto-generated editors would lose their purpose. Regards. Twain.

## Answer

**Georgi** answered on 30 Oct 2023

Hi, Marcos, Thank you for the provided information! Based on this, I attempted to replicate the behaviour. However, on my side, the spinner of the disabled FormItem (NumericTextBox) does not allow for modification of the value. Is it possible for you to modify this REPL sample so the issue is reproducible and send it back to me? This way, I can investigate it locally and come up with suggestions accordingly. I am looking forward to your reply. Kind regards, Georgi Progress Telerik

### Response

**Twain** commented on 30 Oct 2023

Hello Georgi, I conducted a test with part of my code on the example you provided, and it happens exactly as you mentioned. The auto-generated changes respond correctly to 'Enabled="false"'. I will try to replicate exactly the structure and the code that is failing to provide a more comprehensive example. Regards. Marcos.-
