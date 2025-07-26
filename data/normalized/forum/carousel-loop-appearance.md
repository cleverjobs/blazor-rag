# Carousel loop appearance?

## Question

**Bra** asked on 03 Oct 2024

I'm a newbie about to try putting a carousel in my first app. I notice, however, that when the carousel loops back to the beginning, the visual appearance truly is of going back to the beginning. Is there an easy way to make it look, instead, like it's an endless loop? Obviously the buttons would betray the truth, but the images would appear to move forward continuously. Thanks!

## Answer

**Hristian Stefanov** answered on 04 Oct 2024

Hi Bradley, A feature request for the desired functionality has already been submitted on our public feedback portal: Endless Scrolling. I voted for the item on your behalf and raised its priority. You can also subscribe to it to receive email notifications for further status updates. Workaround Currently, the most convenient approach to mitigate the issue with rewinding fast forward/backward is to conditionally stop the animation by applying a custom CSS class. This class will pause the transition animation when transitioning from the initial slide to the last one, or vice versa. This illustrative sample also showcases the dynamic functionality of adding new slides. <TelerikButton OnClick="AddNewItem"> Add New Item </TelerikButton> <TelerikCarousel @ref="@CarouselRef" Class="@(isScrollable ? " ": " my-carousel ")" Data="@CarouselData" Page="@PageIndex" PageChanged="@PageChangedHandler" Width="400px" Height="200px" AutomaticPageChange="false"> <Template> <div class="item"> ID @(context.ID) : @(context.Text) </div> </Template> </TelerikCarousel> <style>.item { background: #3d57d8; color: #fff; font: 36px / 200px sans-serif; text-align: center;
}.my-carousel.k-scrollview-wrap.k-scrollview-animate { transition-duration: 0s;
} </style> @code {
private TelerikCarousel <CarouselModel> CarouselRef;
public bool isScrollable { get; set; }=true;

public int PageIndex=1; public async Task PageChangedHandler(int newPage)
{
if (PageIndex==CarouselData.First().ID && newPage==CarouselData.Last().ID || PageIndex==CarouselData.Last().ID && newPage==CarouselData.First().ID)
{
isScrollable=false;
}
else
{
isScrollable=true;
}
PageIndex=newPage;
} void AddNewItem()
{
CarouselData.Add(new CarouselModel() { ID=CarouselData.Count() + 1, Text="Text " + (CarouselData.Count() + 1) });

isScrollable=false;

CarouselRef.Rebind();
}

public List <CarouselModel> CarouselData=new List <CarouselModel> ()
{
new CarouselModel
{
ID=1,
Text="Text " + 1
},
new CarouselModel
{
ID=2,
Text="Text " + 2
},
new CarouselModel
{
ID=3,
Text="Text " + 3
}
};

public class CarouselModel
{
public int ID { get; set; }
public string Text { get; set; }
}
} Regards, Hristian Stefanov Progress Telerik

### Response

**Bradley** commented on 04 Oct 2024

Well that's disappointing. Given that the request is over a year old and is marked as "Unplanned", I guess I'll have to look elsewhere if I want that functionality.

### Response

**Hristian Stefanov** commented on 07 Oct 2024

Hi Bradley, I'm sorry to hear that my answer didn't completely meet what you are looking for. I admit that the public item is quite old. The reason is that items with higher priority have been addressed during that time. If we come across any better options, I will share them as a comment in the public post. Kind Regards, Hristian
