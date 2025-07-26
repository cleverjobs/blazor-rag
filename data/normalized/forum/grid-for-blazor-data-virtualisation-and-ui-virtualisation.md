# Grid For Blazor Data Virtualisation and UI Virtualisation

## Question

**Ros** asked on 26 Apr 2019

Hi i am die hard WPF developer taking a peek at the grid component of Blazor. I use data and UI virtualisation features of radgridview heavily in my existing WPF apps, and it would be great to have these features available in Blazor. A couple of references here. [https://docs.telerik.com/devtools/wpf/controls/radgridview/features/ui-virtualization.](https://docs.telerik.com/devtools/wpf/controls/radgridview/features/ui-virtualization.) [https://docs.telerik.com/devtools/wpf/controls/radgridview/populating-with-data/populating-datavirtualization.](https://docs.telerik.com/devtools/wpf/controls/radgridview/populating-with-data/populating-datavirtualization.) Is this something that may be considered? Thanks Ross

## Answer

**Joana** answered on 26 Apr 2019

Hi Ross, Thank you for the suggestion. Currently, the Grid supports paging which is actually fetching the data on demand. You could test the functionality in the following link: [https://demos.telerik.com/blazor/grid/paging](https://demos.telerik.com/blazor/grid/paging) [https://docs.telerik.com/blazor/components/grid/paging](https://docs.telerik.com/blazor/components/grid/paging) Indeed, what I could get from the WPF virtualization articles, endless scrolling would be a nice improvement of the user experience. We will definitely revise it and track the demand for such virtual capabilities. Regards, Joana

### Response

**Ross** answered on 29 Apr 2019

Further to this just as a point of reference it may be interesting to look at the relatively recent Angular 7 virtual scroll viewport. [https://blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c](https://blog.angular.io/version-7-of-angular-cli-prompts-virtual-scroll-drag-and-drop-and-more-c594e22e7b8c) I was able to get some rudementry virtual data by listening to the scrolled index changed event which fired everytime the record at the top of the grid changed as it scrolled passed. I then loaded up a page of data as the record count got close to the end and added it to the end of the array. It then appeared nicely when scrolled to. My template implementation is as follows <cdk-virtual-scroll-viewport itemSize="35" fxFlex (scrolledIndexChange)="handler($event)"> <li * cdkVirtualFor="let hero of heroes"> <a routerLink="/detail/{{hero.id}}"> <span class="badge">{{hero.id}}</span> {{hero.name}} </a> </li> </cdk-virtual-scroll-viewport> I use these types of grids a lot and find it really nice being able to scroll through the data. Im sure lots of other people do too and thats why its in Angular 7. Thanks, Ross

### Response

**Joana** answered on 29 Apr 2019

Hi Ross, Thank you for the follow up and for sharing these resources. We highly appreciate such feedback. Once the feature is considered for implementation, we will review all suggestions and the functional specification will cover the use cases. Regards, Joana
