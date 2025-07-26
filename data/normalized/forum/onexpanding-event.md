# OnExpanding Event

## Question

**Sim** asked on 15 Apr 2020

When a menu is shown I need to be able to enable disable the sub menu items, so I need to hook an expanding event before the sub menu is rendered. Is there any plan to add an OnExpanding event that is raised before the sub item is expanded?

## Answer

**Simon** answered on 16 Apr 2020

Ignore/delete this post, I can see that I can do this using a Template. My mindset is still based on WinForms.

### Response

**Marin Bratanov** answered on 16 Apr 2020

Hi Simon, We haven't had requests for such an event before, yet I can think of two ways do to something like this: don't add the child items to the menu until they are needed (might or might not be possible with the given business logic) use a template and cancel the mouseover event. If this is what you did, I'd encourage you to post this here, as it might be interesting to other people too. Regards, Marin Bratanov
