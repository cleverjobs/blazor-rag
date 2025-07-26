# Browser's back button should close the modal (Window)

## Question

**Jas** asked on 11 Jul 2022

When a user clicks the back button on the web browser, especially on mobile, I'd like to close the modal and remain on the same page. Is there a way to achieve this now?

### Response

**Dimo** commented on 14 Jul 2022

Hi Jason, At first I thought the NavigationManager events should help, but it looks like this is not implemented yet, although it was planned for .NET 6. Hopefully we will get it in .NET 7.
