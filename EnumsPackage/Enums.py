from enum import Enum

class Clothing(Enum):
	CLOTHING_Name_TShirt = "T-Shirts + Sweatshirts"
	CLOTHING_Name_CyclingJersey = "Cycling Jerseys"
	CLOTHING_Name_Socks = "Socks"
	CLOTHING_Name_ToteBags = "Tote Bags"
	CLOTHING_Name_ShoppingBags = "Shopping Bags"
	CLOTHING_Name_Jewellery = "Jewellery"
	CLOTHING_Name_Umbrellas = "Umbrellas"

class Homeware(Enum):
	Homeware_Name_ArtPrints = "Art + Prints "
	Homeware_Name_Kitchenware = "Kitchenware"
	Homeware_Name_Home = "Home"
	Homeware_Name_Books = "Books"
	Homeware_Name_Candles = "Candles"
	Homeware_Name_CraftKits = "Craft Kits"
	Homeware_Name_Wellness = "Wellness"
	Homeware_Name_KindfullnessSubscription = "Kindfulness Subscription"

class Stationery(Enum):
	Stationery_Name_GreetingsCards = "Greetings Cards"
	Stationery_Name_BirthdayCards = "Birthday Cards"
	Stationery_Name_CongratulationsCards = "Congratulations Cards"
	Stationery_Name_ThankYouCards = "Thank You Cards"
	Stationery_Name_Notebooks = "Notebooks"
	Stationery_Name_EnamelPinBadges = "Enamel Pin Badges"

class Beauty(Enum):
	Beauty_Name_Face = "Face"
	Beauty_Name_Body = "Body"
	Beauty_Name_Emolyne = "Emolyne"

class DisplayPerPage(Enum):
	Display_per_page_24 = 24
	Display_per_page_36 = 36
	Display_per_page_48= 48

class TshirtsAndSweatShirts(Enum):
    Kelly_Laderer_Team_GB	= "Kelly Laderer Team GB x British Red Cross White Cotton T-Shirt"
    Miles_for_refugees	= "Miles for refugees t-shirt"
    Sound_wave_tshirts	= "Sound wave t-shirts - various songs"
    Dream_Big_Babygrow	= "Dream Big Babygrow"
    Supermundane	= "Unisex organic cotton T-shirt - Supermundane"
    Morag_Myerscough	= "Unisex organic cotton T-shirt - Morag Myerscough"
    Team_GB_x_British_Red_Cross	= "Team GB x British Red Cross Unisex Organic Cotton White T-Shirt"
    Molly_Bland	= "Unisex organic cotton T-shirt - Molly Bland"
    Snail	= "Grow Up Slowly Babygrow - Snail"
    Got_Your_Back	= "Got Your Back - Unisex T-shirt"
    Aleesha_Nandhra	= "Unisex organic cotton T-shirt - Aleesha Nandhra"
    Craig_Karl	= "Unisex organic cotton T-shirt - Craig & Karl"
    Red_Cross_Printed_Cotton_Tshirt	= "Kelli Laderer Team GB x British Red Cross Printed Cotton T-Shirt"
    Nadina_Ali	= "Unisex organic cotton T-shirt - Nadina Ali"
    Grow_Up_Slowly_Snail	= "Grow Up Slowly Snail Children"
    Dream_Big_Giraffe	= "Dream Big Giraffe Children"
    Oversized_Charcoal_Sweater	= "You are enough"
    Love_is_Love	= "Love is Love"
    Dream_Big_Elephant_Swearshirt	= "Dream Big Elephant"

class TshirtsAndSweatShirtsSorting(Enum):
    Featured = "Featured "
    Best_selling = "Best selling "
    Alphabetically_A_to_Z = "Alphabetically, A-Z "
    Alphabetically_Z_to_A = "Alphabetically, Z-A "
    Price_low_to_high = "Price, low to high "
    Price_high_to_low= "Price, high to low "
    Date_old_to_new = "Date, old to new "
    Date_new_to_old= "Date, new to old "

class VirtualGifts(Enum):
    A_food_parcel_for_a_refugee = "A food parcel for a refugee"
    A_wheelchair_for_someone_who_cant_afford_it = "A wheelchair for someone"
    A_hygiene_pack_for_a_refugee = "A hygiene pack for a refugee"
    Essentials_for_a_family_hit_by_floods = "Essentials for a family hit by floods"
    Support_for_someone_with_nowhere = "Support for someone with nowhere to go after leaving hospital"
    Bring_a_family_back_together = "Bring a family back together"
    Warm_clothes_or_a_new_school_uniform = "Warm clothes or a new school uniform"
    A_sleeping_bag_for_someone = "A sleeping bag for someone forced to flee their home in Syria."
    Agricultural_training_for_a_farmer_in_Namibia = "Agricultural training for a farmer in Namibia."
    Full_support_for_a_refugee_arriving_in_the_UK = "Full support for a refugee arriving in the UK"
    One_on_one_advice_and_support = "One-on-one advice and support"
    A_phone_and_mobile_data_for_a_refugee = "A phone and mobile data for a refugee"
    Wrapping_for_refugees = "Wrapping for refugees"

# class CreateAccount(Enum):
# 	CREATEACCOUNT_Name_FirstName = "customer[first_name]"
# 	CREATEACCOUNT_Name_LastName = "customer[last_name]"
# 	CREATEACCOUNT_Name_Email = "register-customer[email]"
# 	CREATEACCOUNT_Name_Password = "register-customer[password]"

# class ResoucesPage(Enum):
# 	RESOURCES_Name_ShowCase = "Showcase"
# 	RESOUCES_Name_ContactUs = "Contact Us"
# 	RESOUCES_Name_OpenCartPartners = "OpenCart Partners"
# 	RESOUCES_Name_OPenCartBooks = "OpenCart Books"