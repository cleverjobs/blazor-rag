# Nodes z-index in 1.4.0 always on top

## Question

**And** asked on 29 Jul 2019

I have same problem with z-index when nodes must be go under top menu bar. But all nodes excluding root node go above on top menu bar. This behavior changes from previous version of Telerik Blazor Components. I recorded video how changes behavior after update components to new version. In old version also not all works correctly. I was must to change z-index to 1000 for my menu bar like this: <div class="main"> <div class="top-row bg-light text-body px-4" id="navbar" style="z-index:1000;"> <div class="logo"> <BreadCrumb></BreadCrumb> </div> <div class="end-container"> <a class="nav-item nav-link" style="display:inline-block;" @onclick="@OnSignOutClicked"> <img src="../images/NavMenu/user.svg" width="32" height="32" /> </a> @if (ServiceContext.User is SuperUserProxy) { <a class="nav-item nav-link" style="display:inline-block;" @onclick="@OnChangeCompanyClicked"> <img src="../images/NavMenu/company-building-company.svg" width="32" height="32" /> </a> } </div> </div> @if (ServiceContext.User is SuperUserProxy && ((SuperUserProxy)ServiceContext.User).SelectedCompany==null) { <CompanySelector CompanyWasSelected="@OnCompanyWasSelected"></CompanySelector> } else { <div class="content px-0"> @Body </div> } </div> But after change z-index to 1000 in older version of TreeView all works fine and I even forget about this. But new version quickly remembered about this strange behavior. Link to my video: [https://andriy.co/download/products/2019-07-29%2019-02-19.mp4](https://andriy.co/download/products/2019-07-29%2019-02-19.mp4)

## Answer

**Marin Bratanov** answered on 30 Jul 2019

Hi Andriy, The expanded nodes are now animated and so they are in an AnimationContainer, whose z-index is above 10000. Thus, you need to take this into account when designing a layout (for example, choose 20000 for the menu bar). You can find such details by examining the rendered HTML of the components. I'm attaching below a screenshot that illustrates this. Regards, Marin Bratanov

### Response

**Andriy** answered on 30 Jul 2019

Hi Marin Thank you very much
