# Blazor Dashboard Project

## Question

**Ste** asked on 23 Nov 2020

I've created a simple dashboard using the Dashboard Project Template and was wondering what's the best approach to having the dashboard update either on a timed basis or data being updated? Should each Blazor Component handle it's own refresh or should we look at doing this at layout level? Cheers

## Answer

**Marin Bratanov** answered on 23 Nov 2020

Hi Steve, This is entirely up to your needs and preferences. For example, if the individual components work with quite different data from one another, perhaps it will make more sense to have each of them request its own data as needed. If, however, most of the data comes from one place and is passed down as parameters to individual components, maybe updating that single place will be significantly easier. What I can suggest as sample resources is the following projects we have that take rather different approaches: the dashboard sample app: [https://demos.telerik.com/blazor-dashboard-app/](https://demos.telerik.com/blazor-dashboard-app/) - there is a dropdown that triggers updates on interval, so you can borrow ideas from the source code. In this case, there are rather few components, and a shared data source is updated. the stocks sample app follows a similar pattern - one place requests data and passes it down the component tree: [https://demos.telerik.com/blazor-financial-portfolio.](https://demos.telerik.com/blazor-financial-portfolio.) The real time data page, however, has its own data source and implements timed updates too, only for a single component (not that there is a signifiant difference in the code, would there have been more components). the Dashboard sample project template from our New Project Wizard: [https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard.](https://docs.telerik.com/blazor-ui/getting-started/vs-integration/new-project-wizard.) It uses a mixed approach - some components take data from their parent, others fetch their own. Regards, Marin Bratanov
