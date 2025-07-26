# Pager fails to render page size in dropdown when total items is equal to current pagesize

## Question

**Pin** asked on 09 Oct 2022

I've made a simple blazor repl demo here: [https://blazorrepl.telerik.com/mmlYatun39gTFEgO21](https://blazorrepl.telerik.com/mmlYatun39gTFEgO21) As you can see, TotalCount is 10, and the current PageSize is also 10. When these values match, the value in the "items per page" dropdown isn't present. Select any other value, and it will be present (for 5, 20, 40). Come back to 10, and again, the value disappears. Image examples, with items per page set to 10, then 5:

## Answer

**Hristian Stefanov** answered on 12 Oct 2022

Hi Matthew, The described behavior is a confirmed bug in the Pager. The value goes blank when also the " PageSize " is not presented in the " PageSizes " list. Here is the public item I created on your behalf for the issue: A blank value appears in the dropdown when PageSize is not within the predefined PageSizes or equals the TotalCount. You are automatically subscribed (as a creator) to receive email notifications for status updates. In the meantime, if a workaround appears, I will contact you immediately here. Lastly, as a small gesture of gratitude for the effort and the reported bug, I added Telerik points to your account. If we can help with anything else, I'm at your disposal. Regards, Hristian Stefanov Progress Telerik

### Response

**Pingu** commented on 12 Oct 2022

Thanks. :)
