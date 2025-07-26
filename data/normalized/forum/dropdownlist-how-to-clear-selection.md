# DropDownList: How to clear selection

## Question

**Joe** asked on 15 May 2025

The user doesn't have to select anything in my drop down. So, if they select something and change their mind and want to clear it... how do I do it? <TelerikDropDownList @bind-Value="@SessionOptionIndex1" Data="@SessionOption1Items" TextField="Name" ValueField="Id" />

### Response

**Anislav** commented on 16 May 2025

Hi Joel, The TelerikDropDownList does not include a built-in ClearButton feature. A possible workaround is to include a "None" or equivalent placeholder item as the first option in SessionOption1Items to allow users to clear their selection. Regards, Anislav Atanasov

### Response

**Hristian Stefanov** commented on 16 May 2025

Hi all, Indeed, the TelerikDropDownList does not include a built-in clear button. However, it is still achievable with a standard TelerikButton and some positioning styling: How to Add a Clear Button Inside DropDownList. Kind Regards, Hristian
