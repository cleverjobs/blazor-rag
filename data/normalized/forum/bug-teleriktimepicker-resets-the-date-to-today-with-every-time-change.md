# BUG: TelerikTimePicker resets the date to Today with every time change

## Question

**Rol** asked on 27 Jan 2022

The component can bind to a DateTime variable. The expected behaviour is that only the time part is updated, so that the actual date is preserved. For instance if I want to want to let the user set a time for an appointment tomorrow, the appointment should not move to today because the time was changed

## Answer

**Dimo** answered on 02 Feb 2022

Hi Roland, The TimePicker assumes that the application logic is not interested in the Date portion of the value. If the Date portion matters, there are some options: Use a DateTimePicker instead, so that the Date portion is visible and controllable by the user. Ignore the new Date portion and apply only the new Time portion in ValueChanged. Set and store the Date portion separately, so that you can start ignoring the Date portion in the TimePicker value. On a side note, the TimePicker will also support TimeOnly in the future. Regards, Dimo Progress Telerik

### Response

**Roland** commented on 02 Feb 2022

"The TimePicker assumes that the application logic is not interested in the Date portion of the value." Like when you change the time of an appointment on a given day? Not a good assumption in my book. "Set and store the Date portion separately". That is my current workaround. "TimePicker will also support TimeOnly". That would be more predictable, but I still think that a TimePicker that (also) supports DateTime databinding is more flexible and should never overwrite the date part.

### Response

**Shahram** commented on 20 Jun 2023

Hi Roland, Thanks for your comment and suggesting a few workarounds. But, Do you have a plan to fix this bug? It seems that " TimePicker assumes that the application logic is not interested in the Date portion of the value" is not a valid assumption.

### Response

**Marin Bratanov** answered on 30 Jan 2022

Hi Roland, The TimePicker uses the Date portion of the provided DateTime field. If the NOW button is clicked, however, the date portion will be replaced with the current one. If you want to customize the behavior, you can use the ValueChanged event to transfer only portions of the DateTime object as your business logic requires. Regards, Marin Bratanov

### Response

**Roland** commented on 31 Jan 2022

It is not just the NOW button, if you enter the value manually the date is changed.
