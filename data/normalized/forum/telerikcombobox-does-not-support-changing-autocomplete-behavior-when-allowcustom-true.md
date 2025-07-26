# TelerikComboBox does not support changing AutoComplete behavior when AllowCustom=true

## Question

**Ale** asked on 15 Mar 2022

When AllowCustom=true, the browser treats it like a textbox and shows Auto Complete choices, yet unlike the TelerikTextbox which has an AutoComplete property which allows us to turn it off, there is no corresponding property for TelerikComboBox, and thus no way for us to disable browser autocomplete for it, aside from setting AllowCustom to false.

### Response

**Nadezhda Tacheva** commented on 18 Mar 2022

Hi Alex, By design, regardless of whether or not the AllowCustom is enabled, the input of the ComboBox has autocomplete="off" which on my end seems to behave as expected. I am testing locally and in the live demo as well. Could you please share some more details for the product and browser version you are using, so we can investigate if there is some issue? Please also send us your exact configuration of the ComboBox, so we can replicate the scenario as close as possible. A video of the behavior you are experiencing could also be useful. Thank you in advance! I'll be looking forward to hearing from you!
