# password box

## Question

**kha** asked on 04 Feb 2020

Hi, is there any way to make TextBox into a Password box without having any difference with TextBox i found something in here [https://www.telerik.com/forums/password-char](https://www.telerik.com/forums/password-char) but its not what i want i also used this code <span class="k-textbox-container telerik-blazor"> <input id="641f9bd0-2fbe-483d-9279-2da83c4f397a" tabindex="0" type="password" aria-disabled="false" class="k-textbox "> <label for="641f9bd0-2fbe-483d-9279-2da83c4f397a" class="k-label">Passowrd</label> </span> but it wasnt useful either since it's not exactly like TelerikTextBox so is there any suggestion on how to make it happen and still be same as TelerikTextBox ?

## Answer

**Marin Bratanov** answered on 04 Feb 2020

Hi Khashayar, At the moment, using a class to style a "regular" input is the way to do this. You can Follow the implementation of additional parameters for the input (such as Type which would let it become a password box) here: [https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly.](https://feedback.telerik.com/blazor/1416922-add-to-teleriktextbox-more-parameters-such-as-type-autocomplete-required-readonly.) Regards, Marin Bratanov
