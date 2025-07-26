# 2.26 bootstrap theme missing .k-widget.form-control padding override

## Question

**RobRob** asked on 05 Aug 2021

Hi, in 2.25 I was able to use bootstrap input-group to make the following numeric input: <div class="row"> <div class="col-6"> <label for="inputTest" class="col-form-label-sm"> Label </label> <div class="input-group flex-nowrap"> <div class="input-group-prepend"> <span class="input-group-text"> $ </span> </div> <TelerikNumericTextBox Class="form-control" @bind-Value="number" Id="inputTest" /> </div> </div> </div> In 2.26 the kendo-bootstrap-theme/all.css seems to be missing a .k-widget.form-control css override of padding:0 to make this work. Is this intended or a bug?

### Response

**Baires** commented on 05 Aug 2021

We also had some random style issues here and decided to rollback to 2.25.0

### Response

**Tony** commented on 09 Aug 2021

We upgraded our project to 2.26 last week and also discovered the form-control class issues. We have a ton of forms and each control uses the "form-control" class, and a lot of things are broken now. 1. Previously, controls would be 100% width, now they have a default width unless explicitly defined and therefore render right next to the label instead of below. 2. The k-widget padding issue. We are seeing this cause the rendering issues with Dropdown lists, Date Inputs, Date Pickers, etc. Theoretically, we could add the .k-widget.form-control 0 padding override to our site css to fix the rendering issues, but that wasn't the only form-control override that was removed between 2.25 and 2.26 so it's hard to tell if any of the other override removals have not-quite-as obvious ramifications that will come back to bite us.

## Answer

**Ivan Zhekov** answered on 10 Aug 2021

Rob, Baires, Tony, and anyone else who's reading: This is intended change and not a bug and here is why: with the migration from Bootstrap 4 based theme to Bootstrap 5 based theme there were numerous changes (some of the breaking, since it's major version) and supporting third party classes in our product became nonviable. In addition, we are developing our own sizing system for inputs and the bootstrap forms are interfering when both are applied. Since we do not own the class names (not part of our products), we can not control the cascade, specificity or actual styling of those class names. It's worth noting that for that very same reason, we've went with prefixed class names -- to denote their part of the broader Kendo UI and Telerik UI suites. No one should expect that applying, say `k-combobox` to a DevExpress control will yield any consistent result, and vice versa. Thus, we decided to not provide additional overrides to any third party class names that can be applied to Kendo UI or Telerik UI components, due to the unexpected outcome. How can this be solved? It's quite easy, actually, you as developers know where the components in question (mostly form components) are going to be placed and what the expected result should be. For instance, if you need the components to be 100% wide, you can do so by adding some styling, like Rob and Tony said they could do. Note: the width is by far, not the only issue. There is also the difference in `display`... A much better approach, would be to not mix those class names together. We've went trough a good amount of effort to align visually our kendo-theme-bootstrap theme with the Bootstrap framework. As I suppose any vendor who provides components... I suppose the idea is indeed tempting: I can mix and match this from this framework and that from that framework. If you pardon the comparison, it does sound like taking a V12 engine from a Ferrari and sticking it in a Fiat 500 -- something is bound to go wrong. To continue with the better approach, if you find that something is missing in Telerik UI suite, you can ask for it: while we already have a backlog, feedback from customers does help to prioritize. Which brings me to the question: why do you need to apply bootstrap class names to style Telerik UI components? What do you want to get out of it? If you need the looks: we have a theme for that. If you fancy the form layout, we have that covered -- [https://demos.telerik.com/blazor-ui/form/overview.](https://demos.telerik.com/blazor-ui/form/overview.) If you fancy the sizing, we are working on that. If you just need the width to be 100%, then a simple styling should suffice. Regards, Ivan Zhekov

### Response

**Rob** commented on 10 Aug 2021

Thanks Ivan, I suspected as much. I am sure keeping up with bootstrap would be a big drain on resources, I can understand that. The problem I now face is that it's now me that needs to do the work of finding out what styling changes are needed, or re-write my interface without these input-group features that I heavily use (since the Telerik controls don't have an equivalent), or remove the Telerik integration entirely and just use standard bootstrap controls! This is now the decision I have to make. Finally, while I understand and don't fault this direction you're taking, I don't appreciate the breaking change without any communication until days after the release!

### Response

**Ivan Zhekov** commented on 13 Aug 2021

Rob, you are right about the communication -- rarely we've done worse job in communicating what is about to change. That being said, we can still assist. Can you attach a screenshot of what you want the components to look like? In particular, I would like to see (a picture) of how you use bootstrap input-group with Telerik UI components. Not to downplay what input group does, but it's an over-glorified horizontal layout container that can arrange inputs and buttons next to each other. To us, adding styles for input-group like structure will be a no-brainer and little effort. Besides, we've already have implemented something like that for Kendo UI for Angular (but it's called adornments, for some bizarre Angular naming reason) -- [https://www.telerik.com/kendo-angular-ui/components/inputs/textbox/adornments/.](https://www.telerik.com/kendo-angular-ui/components/inputs/textbox/adornments/.) I know that's not exactly an input group. It's more of Angular Design Team's suggestion of how composite looking inputs should be made. The point here is -- you ask, we can deliver. And especially in the case of an input group, that can be a very fast delivery. There is a dev version of the themes each monday (that is, if Lerna is feeling like releasing).

### Response

**Rob** commented on 20 Aug 2021

Thanks Ivan, adornments look nice and would be acceptable. I have really only two use cases I believe, a prefix display for a TextBox (usually $ on a numeric textbox), as well as a button attached to another control, mostly textbox also but occasionally DatePicker to give a one-click access to Now. Here are a few pictures:

### Response

**Ivan Zhekov** commented on 26 Aug 2021

We have about two weeks in this six weeks cycle. I think it's plenty for an input group. I will write back once we've made some progress.
