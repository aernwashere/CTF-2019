@extends('layouts.header')
@section('content')

<!-- welcome use this css -->
<link rel="stylesheet" href="css/index.css">

<!-- product use this css -->
<link rel="stylesheet" href="css/product.css">
<link rel="stylesheet" href="css/price-range.css">
<link rel="stylesheet" href="css/use-product.css">
<link rel="stylesheet" href="css/elegant-font/html-css/style.css">
<link rel="stylesheet" href="css/star-rating-svg.css">
<!-- product use this css -->

<section class="hero hero-image is-fullheight">
    <div class="hero-body">
        <div class="container">
            <div data-aos="zoom-in" data-aos-once="true" class="has-text-centered has-text-grey-darker">
                <p class="is-size-1 is-size-3-mobile">Book Your Activity Now!</p>
                <p class="is-size-5 is-size-7-mobile has-text-centered">We are Zooka, The Most Popular dive and watersports provider in Tanjung Benoa, Bali<br>We have a lot of underwater and watersport activities with very cheap and suitable price</p>
            </div>
            <div class="container">
                <div class="columns is-centered is-vcentered search-home">
                    <div data-aos="fade-up" data-aos-delay="300" data-aos-once="true" class="column is-8">
                        <div class="input-wrapper">
                            <input type="text" class="search" placeholder="Search..." name="search" id="search" data-list="#mylist"></input>
                        </div>
                        <ul id="mylist"></ul>
                    </div>
                </div>
            </div>
            <!--/container-->
            <div class="search-bottom"></div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <div class="columns">
            <div class="column is-three-quarters">
                <p class="is-size-3 has-text-weight-semibold is-size-5-touch">Explore Category </p>
            </div>
        </div>

        <div class="columns is-mobile is-multiline is-vcentered">
            <div class="column is-one-quarter-tablet is-three-quarters-mobile">
                <a href="{{url("/product")}}">
                    <div class="box is-radiusless is-left-paddingless hvr-shadow">
                        <article class="media explore">
                            <div class="media-left">
                                <figure class="image is-96x96 img-explore">
                                    <img src="{{asset("image/watersports.jpg")}}" alt="Image">
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p class="is-size-4 is-size-6-touch">Watersports</p>
                                </div>
                            </div>
                        </article>
                    </div>
                </a>
            </div>
            <!--/column-->
            <div class="column is-one-quarter-tablet is-three-quarters-mobile">
                <a href="{{url("/product")}}">
                    <div class="box is-radiusless is-left-paddingless hvr-shadow">
                        <article class="media explore">
                            <div class="media-left">
                                <figure class="image is-96x96">
                                    <img src="{{asset("image/underwater.jpg")}}" alt="Image">
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p class="is-size-4 is-size-6-touch">Underwater</p>
                                </div>
                            </div>
                        </article>
                    </div>
                </a>
            </div>
            <!--/column-->
            <div class="column is-one-quarter-tablet is-three-quarters-mobile">
                <a href="{{url("/product")}}">
                    <div class="box is-radiusless is-left-paddingless hvr-shadow">
                        <article class="media explore">
                            <div class="media-left">
                                <figure class="image is-96x96">
                                    <img src="{{asset("image/package.jpg")}}" alt="Image">
                                </figure>
                            </div>
                            <div class="media-content">
                                <div class="content">
                                    <p class="is-size-4 is-size-6-touch">Packages</p>
                                </div>
                            </div>
                        </article>
                    </div>
                </a>
            </div>
            <!--/column-->
        </div>
        <!--/columns-->
    </div>
    <!--/container-->
</section>

<section class="section">
    <div data-aos="fade-up" data-aos-once="true" class="container">
        <p class="title is-size-5-touch">Introducing Zooka's Activities</p>
        <p class="subtitle is-size-6 is-size-7-touch">Amazing activities make you enjoy the sea and the beach at Tanjung - Bali</p>
        <div class="columns">
            <div class="column">
                <figure class="image is-3by1">
                    <img src="{{asset("image/welcome-intro.jpg")}}">
                </figure>
            </div>
            <!--/column-->
        </div>
        <!--/columns-->
    </div>
    <!--/container-->
</section>

<section class="section">
    <div class="container">
        <p class="title is-size-5-touch">Recomended for you</p>

        <!-- Swiper -->
        <div class="swiper-container">
            <div class="swiper-wrapper">
                @foreach($product as $produk)
                <div class="swiper-slide">

                    <div class="card hvr-shadow">
                        <div class="card-image is-clipped is-relative is-overlay">
                            <figure class="image is-1by1">
                                <img class="img-fit" src="{{asset('storage/product/')}}/{{$produk->image}}" alt="Placeholder image">
                            </figure>
                            <div class="block2-overlay trans-0-4">
                                <a href="#" class="hov-pointer trans-0-4 is-size-4 {{!Auth::guest() && Auth::user()->wishlist->where('product_id',$produk->id)->where
                  ('user_id',Auth::user()->id)->count() ? "block2-btn-towishlist" : "block2-btn-addwishlist"}}" data-model-id="{{$produk->id}}" id="love{{$produk->id}}">
                                    <i class="icon-wishlist icon_heart_alt" aria-hidden="true"></i>
                                    <i class="icon-wishlist icon_heart dis-none" aria-hidden="true"></i>
                                </a>
                                <div class="block2-btn-detail w-size1 trans-0-4">
                                    <a class="get-product" href="{{url("/product/{$produk->slug}")}}">Details</a>
                                </div>
                            </div>
                        </div>
                        <div class="card-content">
                            <div class="content has-text-centered mtb-15">
                                <p class="title is-size-6 is-size-7-touch has-text-centered is-marginless has-text-good-night">{{ucwords(str_limit($produk->name,18))}}</p>
                                <p class="is-size-7 is-marginless is-hidden-mobile">
                                    <span class="has-text-eye-of-newt has-text-line-through"> IDR. 700.000 </span>
                                    <span class="has-text-danger has-text-weight-bold">{{"IDR. " . number_format($produk->price,0,',','.')}}</span>
                                </p>
                                <p class="is-size-7 is-marginless is-hidden-desktop">
                                    <span class="has-text-eye-of-newt has-text-line-through"> IDR. 700.000 </span><br>
                                    <span class="has-text-danger has-text-weight-bold">{{"IDR. " . number_format($produk->price,0,',','.')}}</span>
                                </p>
                                <p class="is-size-7 is-marginless">
                                    <span class="rating-product" data-rating="{{$produk->averageRating}}"></span>
                                </p>
                            </div>
                            <!--/content-->
                        </div>
                        <!--/card-content-->
                    </div>
                    <!--/card-->

                </div><!-- swipper-slide -->
                @endforeach
            </div>
            <!--/swipper-wrapper-->
        </div>
        <!--/swipper-container-->
        <!-- Swiper -->
        <div class="swiper-button-next rounded-next has-text-centered"><i class="far fa-angle-right fa-3x"></i></div>
        <div class="swiper-button-prev rounded-back has-text-centered"><i class="far fa-angle-left fa-3x"></i></div>
    </div>
    <!--/container-->

    <div class="container m-t-30">
        <div class="columns">
            <div class="column">
                <figure class="image is-3by1">
                    <img src="{{asset("image/welcome-recom.jpg")}}">
                </figure>
            </div>
            <!--/column-->
        </div>
        <!--/columns-->
    </div>
    <!--/container-->
</section>

<section class="section">
    <div class="container">
        <p class="title is-size-5-touch">Top-rated experiences</p>
        <p class="subtitle is-size-6 is-size-7-touch">Book activities lead by local hosts on your next trip</p>
        <div class="card-content item-padding">


            <!-- ITEM -->
            <div class="columns is-multiline is-mobile">
                @foreach($product as $produk)
                <div class="column item-padding is-half-mobile is-half-tablet is-one-fifth-fullhd is-one-fifth-desktop is-one-quarter-fullhd">
                    <div class="card hvr-shadow">
                        <div class="card-image is-clipped is-relative is-overlay">
                            <figure class="image is-1by1">
                                <img class="img-fit" src="{{asset('storage/product/')}}/{{$produk->image}}" alt="Placeholder image">
                            </figure>
                            <div class="block2-overlay trans-0-4">
                                <a href="#" class="hov-pointer trans-0-4 is-size-4 {{!Auth::guest() && Auth::user()->wishlist->where('product_id',$produk->id)->where
                  ('user_id',Auth::user()->id)->count() ? "block2-btn-towishlist" : "block2-btn-addwishlist"}}" data-model-id="{{$produk->id}}" id="love{{$produk->id}}">
                                    <i class="icon-wishlist icon_heart_alt" aria-hidden="true"></i>
                                    <i class="icon-wishlist icon_heart dis-none" aria-hidden="true"></i>
                                </a>
                                <div class="block2-btn-detail w-size1 trans-0-4">
                                    <a class="get-product" href="{{url("/product/{$produk->slug}")}}">Details</a>
                                </div>
                            </div>
                        </div>
                        <div class="card-content">
                            <div class="content has-text-centered mtb-15">
                                <p class="title is-size-6 is-size-7-touch has-text-centered is-marginless has-text-good-night">{{ucwords(str_limit($produk->name,18))}}</p>
                                <p class="is-size-7 is-marginless is-hidden-mobile">
                                    <span class="has-text-eye-of-newt has-text-line-through"> IDR. 700.000 </span>
                                    <span class="has-text-danger has-text-weight-bold">{{"IDR. " . number_format($produk->price,0,',','.')}}</span>
                                </p>
                                <p class="is-size-7 is-marginless is-hidden-desktop">
                                    <span class="has-text-eye-of-newt has-text-line-through"> IDR. 700.000 </span><br>
                                    <span class="has-text-danger has-text-weight-bold">{{"IDR. " . number_format($produk->price,0,',','.')}}</span>
                                </p>
                                <p class="is-size-7 is-marginless">
                                    <span class="rating-product" data-rating="{{$produk->averageRating}}"></span>
                                </p>
                            </div>
                            <!--/content-->
                        </div>
                        <!--/card-content-->
                    </div>
                    <!--/card-->
                </div>
                <!--/column-->
                @endforeach
                <!-- ITEM -->
            </div>
            <!--/columns is-multiline-->


            <div class="link">
                <a class="is-size-6 is-primary under" href="#">Show all experiences</a>
                <span class="icon is-small">
                    <i class="fas fa-angle-right" aria-hidden="true"></i>
                </span>
            </div>
        </div>
    </div>
    <!--/container-->
</section>

<section class="section">
    <div class="container">
        <p class="title is-size-5-touch">Head to the beach</p>

        <!-- Swiper -->
        <div class="swiper-container">
            <div class="swiper-wrapper">
                @foreach($product as $produk)
                <div class="swiper-slide">

                    <div class="card hvr-shadow">
                        <div class="card-image is-clipped is-relative is-overlay">
                            <figure class="image is-1by1">
                                <img class="img-fit" src="{{asset('storage/product/')}}/{{$produk->image}}" alt="Placeholder image">
                            </figure>
                            <div class="block2-overlay trans-0-4">
                                <a href="#" class="hov-pointer trans-0-4 is-size-4 {{!Auth::guest() && Auth::user()->wishlist->where('product_id',$produk->id)->where
                  ('user_id',Auth::user()->id)->count() ? "block2-btn-towishlist" : "block2-btn-addwishlist"}}" data-model-id="{{$produk->id}}" id="love{{$produk->id}}">
                                    <i class="icon-wishlist icon_heart_alt" aria-hidden="true"></i>
                                    <i class="icon-wishlist icon_heart dis-none" aria-hidden="true"></i>
                                </a>
                                <div class="block2-btn-detail w-size1 trans-0-4">
                                    <a class="get-product" href="{{url("/product/{$produk->slug}")}}">Details</a>
                                </div>
                            </div>
                        </div>
                        <div class="card-content">
                            <div class="content has-text-centered mtb-15">
                                <p class="title is-size-6 is-size-7-touch has-text-centered is-marginless has-text-good-night">{{ucwords(str_limit($produk->name,18))}}</p>
                                <p class="is-size-7 is-marginless is-hidden-mobile">
                                    <span class="has-text-eye-of-newt has-text-line-through"> IDR. 700.000 </span>
                                    <span class="has-text-danger has-text-weight-bold">{{"IDR. " . number_format($produk->price,0,',','.')}}</span>
                                </p>
                                <p class="is-size-7 is-marginless is-hidden-desktop">
                                    <span class="has-text-eye-of-newt has-text-line-through"> IDR. 700.000 </span><br>
                                    <span class="has-text-danger has-text-weight-bold">{{"IDR. " . number_format($produk->price,0,',','.')}}</span>
                                </p>
                                <p class="is-size-7 is-marginless">
                                    <span class="rating-product" data-rating="{{$produk->averageRating}}"></span>
                                </p>
                            </div>
                            <!--/content-->
                        </div>
                        <!--/card-content-->
                    </div>
                    <!--/card-->

                </div><!-- swipper-slide -->
                @endforeach
            </div>
            <!--/swipper-wrapper-->
        </div>
        <!--/swipper-container-->
        <!-- Swiper -->
        <div class="swiper-button-next rounded-next has-text-centered"><i class="far fa-angle-right fa-3x"></i></div>
        <div class="swiper-button-prev rounded-back has-text-centered"><i class="far fa-angle-left fa-3x"></i></div>
    </div>
    <!--/container-->
</section>

<section class="section">
    <div class="container">
        <p data-aos="fade-up" data-aos-once="true" class="title is-size-5-touch">Why choose Us?</p>
        <p data-aos="fade-up" data-aos-once="true" class="subtitle is-size-6 is-size-7-touch">Great value only for you by online booking our activities</p>
        <div class="columns">
            <div data-aos="zoom-in" data-aos-delay="300" data-aos-once="true" class="column is-one-third has-text-centered">
                <div class="card is-shadowless">
                    <div class="card-content">
                        <i class="fas fa-shuttle-van fa-5x"></i>
                        <p><br></p>
                        <p class="title is-size-5">Free Transport</p>
                        <p class="subtitle is-size-6">We provide you free transport from your hotel to Zooka and put you back to hotel, by order our activities from this website</p>
                    </div>
                </div>
            </div>
            <div data-aos="zoom-in" data-aos-delay="300" data-aos-once="true" class="column is-one-third has-text-centered">
                <div class="card is-shadowless">
                    <div class="card-content">
                        <i class="fas fa-hands-helping fa-5x"></i>
                        <p><br></p>
                        <p class="title is-size-5">Insurance Guarantee</p>
                        <p class="subtitle is-size-6">Don't worry for play in our watersports and underwater activities, you have protected by our insurance up to IDR 80 million</p>
                    </div>
                </div>
            </div>
            <div data-aos="zoom-in" data-aos-delay="300" data-aos-once="true" class="column is-one-third has-text-centered">
                <div class="card is-shadowless">
                    <div class="card-content">
                        <i class="fas fa-money-check-alt fa-5x"></i>
                        <p><br></p>
                        <p class="title is-size-5">Easy Payment</p>
                        <p class="subtitle is-size-6">Take your experience in our easy payment, we provide secure and reachable payment methods that support cash, onsite and down payment</p>
                    </div>
                </div>
            </div>
        </div>
    </div>
</section>

<section class="section">
    <div class="container">
        <p data-aos="fade-up" data-aos-once="true" class="title is-size-5-touch">Payment Method</p>
        <p data-aos="fade-up" data-aos-once="true" class="subtitle is-size-6 is-size-7-touch">Making it easier for you to pay with many payment methods</p>
        <center>
            <div data-aos="fade-up" data-aos-delay="300" data-aos-once="true" class="columns is-mobile is-multiline">
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/mastercard.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/visa.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/jcb.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/amex.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/mandiri.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/bca.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/syariah.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/cimbniaga.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/bni.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/bri.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/ocbc.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/mega.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/permata.png">
                    </figure>
                </div>
                <!--/column-->
                <div class="column is-one-third-mobile is-one-quarter-tablet is-2-desktop">
                    <figure class="image is-96x96">
                        <img src="image/payment-method/hsbc.png">
                    </figure>
                </div>
                <!--/column-->
            </div>
            <!--/columns is-mobile is-multiline-->
        </center>
    </div>
</section>
<div id="about-us"></div>
<section class="section padding-map">
    <div class="container">
        <p data-aos="fade-up" data-aos-once="true" class="title is-size-5-touch">Location</p>
        <p data-aos="fade-up" data-aos-once="true" class="subtitle is-size-6 is-size-7-touch">Let's find our office here</p>
        <div data-aos="fade-up" data-aos-delay="300" data-aos-once="true" class="columns is-centered">
            <div class="column">
                <div id="map" style="width:100%;height:30rem;"></div>
            </div>
        </div>
    </div>
</section>

<!-- avatar -->
<section class="section">
    <div class="container">
        <p data-aos="fade-up" data-aos-once="true" class="title is-size-5-touch">Our Team</p>
        <p data-aos="fade-up" data-aos-once="true" class="subtitle is-size-6 is-size-7-touch">Thankful for our partner with fully responsibility and hardwork until today</p>
        <div class="columns is-centered is-mobile is-multiline">
            <div data-aos="zoom-in-up" data-aos-delay="300" data-aos-once="true" class="column is-half-mobile has-text-centered">
                <center>
                    <figure class="image is-256x256 avatar-padding">
                        <img class="is-rounded" src="https://bulma.io/images/placeholders/256x256.png">
                    </figure>
                </center>
                <p class="subtitle is-size-5 is-size-7-touch">Leader</p>
            </div>
            <div data-aos="zoom-in-up" data-aos-delay="300" data-aos-once="true" class="column is-half-mobile has-text-centered">
                <center>
                    <figure class="image is-256x256 avatar-padding">
                        <img class="is-rounded" src="https://bulma.io/images/placeholders/256x256.png">
                    </figure>
                </center>
                <p class="subtitle is-size-5 is-size-7-touch">Backend</p>
            </div>
            <div data-aos="zoom-in-up" data-aos-delay="300" data-aos-once="true" class="column is-half-mobile has-text-centered">
                <center>
                    <figure class="image is-256x256 avatar-padding">
                        <img class="is-rounded" src="https://bulma.io/images/placeholders/256x256.png">
                    </figure>
                </center>
                <p class="subtitle is-size-5 is-size-7-touch">Frontend</p>
            </div>
            <div data-aos="zoom-in-up" data-aos-delay="300" data-aos-once="true" class="column is-half-mobile has-text-centered">
                <center>
                    <figure class="image is-256x256 avatar-padding">
                        <img class="is-rounded" src="https://bulma.io/images/placeholders/256x256.png">
                    </figure>
                </center>
                <p class="subtitle is-size-5 is-size-7-touch">Frontend</p>
            </div>
            <div data-aos="zoom-in-up" data-aos-delay="300" data-aos-once="true" class="column is-half-mobile has-text-centered">
                <center>
                    <figure class="image is-256x256 avatar-padding">
                        <img class="is-rounded" src="https://bulma.io/images/placeholders/256x256.png">
                    </figure>
                </center>
                <p class="subtitle is-size-5 is-size-7-touch">UI / UX</p>
            </div>
        </div>
    </div>
</section>
<!-- avatar -->

<script>
    function initMap() {
        var myLatLng = {
            lat: -8.753199,
            lng: 115.219950
        };
        var map = new google.maps.Map(document.getElementById('map'), {
            zoom: 17,
            center: myLatLng,
            mapTypeId: google.maps.MapTypeId.HYBRID
        });
        var marker = new google.maps.Marker({
            position: myLatLng,
            map: map,
        });
    }

</script>

<script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyAF9BOyzOCk8jVFsQ9z1qhxzt3t35z0AR4&callback=initMap" async defer></script>
<script src="{{asset('aos-master/dist/aos.js')}}"></script>
<script src="{{asset('js/jquery.star-rating-svg.js')}}"></script>
<script>
    AOS.init();

</script>

<script>
    $(".rating-product").starRating({
        totalStars: 5,
        starShape: 'rounded',
        readOnly: true,
        starSize: 13,
        emptyColor: 'lightgray',
        activeColor: '#CCCC00',
        useGradient: false
    });
</script>

<script src='{{asset('js/awesomplete.min.js')}}'></script>
<script src='{{asset('js/search-zooka.js')}}'></script>
<script src="{{ asset('js/product/swiper.min.js')}}"></script>
<script src="{{ asset('js/product/slider.js') }}"></script>
@include('layouts.footer1')
@endsection
