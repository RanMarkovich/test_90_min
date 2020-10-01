class TestData:

    # ===================================HOME PAGE DATA===================================#
    HOME_PAGE_URL = "https://www.90min.com/"
    HOME_PAGE_SPANISH_URL = "https://www.90min.com/es?georedirect=false"
    HOME_PAGE_EXPECTED_HEADERS_LINKS = \
        ['Premier League', 'Transfers', 'Champions League', 'FanVoice', 'The Switch', 'EFL', 'La Liga', 'Serie A',
         'More']

    SVG_FACEBOOK_ICON = "M10.17,64V36H0V24.42H10.17V15.59c0-10,6-15.59,15.14-15.59a61.9,61.9,0,0,1,9,.78v9.86H29.23c-5,0-6.53,3.09-6.53,6.26v7.52H33.81L32,36H22.7V64Z"
    SVG_TWITTER_ICON = "M20.1,52c24.15,0,37.37-20,37.37-37.37,0-.56,0-1.12,0-1.69A26.73,26.73,0,0,0,64,6.17a26.87,26.87,0,0,1-7.56,2.08A13.21,13.21,0,0,0,62.23,1a26.1,26.1,0,0,1-8.35,3.18,13.13,13.13,0,0,0-22.71,9,14.8,14.8,0,0,0,.33,3A37.26,37.26,0,0,1,4.43,2.41,13.17,13.17,0,0,0,8.5,20a13.38,13.38,0,0,1-5.94-1.64v.18A13.15,13.15,0,0,0,13.09,31.37a12.73,12.73,0,0,1-3.46.46,12.37,12.37,0,0,1-2.46-.23,13.13,13.13,0,0,0,12.27,9.12A26.38,26.38,0,0,1,3.12,46.35,26.82,26.82,0,0,1,0,46.18,37.41,37.41,0,0,0,20.1,52"
    SVG_INSTAGRAM_ICON_A = "M32,5.77c8.54,0,9.56,0,12.93.18a17.81,17.81,0,0,1,5.94,1.1,9.87,9.87,0,0,1,3.68,2.4A9.87,9.87,0,0,1,57,13.13a17.81,17.81,0,0,1,1.1,5.94c.15,3.37.18,4.39.18,12.93s0,9.56-.18,12.93A17.81,17.81,0,0,1,57,50.87,10.66,10.66,0,0,1,50.87,57a17.81,17.81,0,0,1-5.94,1.1c-3.37.15-4.39.18-12.93.18s-9.56,0-12.93-.18A17.81,17.81,0,0,1,13.13,57a9.87,9.87,0,0,1-3.68-2.4,9.87,9.87,0,0,1-2.4-3.68A17.81,17.81,0,0,1,6,44.93C5.8,41.56,5.77,40.54,5.77,32s0-9.56.18-12.93a17.81,17.81,0,0,1,1.1-5.94,9.87,9.87,0,0,1,2.4-3.68,9.87,9.87,0,0,1,3.68-2.4A17.81,17.81,0,0,1,19.07,6c3.37-.15,4.39-.18,12.93-.18M32,0c-8.69,0-9.78,0-13.19.19A23.59,23.59,0,0,0,11,1.68,15.67,15.67,0,0,0,5.37,5.37,15.67,15.67,0,0,0,1.68,11,23.59,23.59,0,0,0,.19,18.81C0,22.22,0,23.31,0,32s0,9.78.19,13.19A23.59,23.59,0,0,0,1.68,53a15.67,15.67,0,0,0,3.69,5.67A15.67,15.67,0,0,0,11,62.32a23.59,23.59,0,0,0,7.77,1.49C22.22,64,23.31,64,32,64s9.78,0,13.19-.19A23.59,23.59,0,0,0,53,62.32,16.34,16.34,0,0,0,62.32,53a23.59,23.59,0,0,0,1.49-7.77C64,41.78,64,40.69,64,32s0-9.78-.19-13.19A23.59,23.59,0,0,0,62.32,11a15.67,15.67,0,0,0-3.69-5.67A15.67,15.67,0,0,0,53,1.68,23.59,23.59,0,0,0,45.19.19C41.78,0,40.69,0,32,0Z"
    SVG_INSTAGRAM_ICON_B = "M32,15.57A16.43,16.43,0,1,0,48.43,32,16.42,16.42,0,0,0,32,15.57Zm0,27.1A10.67,10.67,0,1,1,42.67,32,10.67,10.67,0,0,1,32,42.67Z"
    SVG_YOUTUBE_ICON = "M62.66,7A8,8,0,0,0,57,1.35C52,0,32,0,32,0S12,0,7,1.35A8,8,0,0,0,1.34,7C0,12.06,0,22.55,0,22.55S0,33,1.34,38.05A8,8,0,0,0,7,43.74c5,1.35,25,1.35,25,1.35s20,0,25-1.35a8,8,0,0,0,5.66-5.69C64,33,64,22.55,64,22.55S64,12.06,62.66,7Zm-37.21,25V13l16.73,9.52Z"
    SVG_RSS_ICON = "M51.5,63.7a50.75,50.75,0,0,0-15-36.2A50.75,50.75,0,0,0,.3,12.5V0A63.29,63.29,0,0,1,45.4,18.6a63.33,63.33,0,0,1,18.7,45H51.5Zm-21.4,0A30,30,0,0,0,.1,33.8V21.2A42.61,42.61,0,0,1,42.7,63.7ZM9,64a9,9,0,1,1,9-9A9,9,0,0,1,9,64Z"

    DROP_DOWN_RGB_COLOR_ON_MOUSE_HOVER = 'rgba(254, 80, 0, 1)'

    # ===================================ARSENAL PAGE DATA===================================#
    ARSENAL_PAGE_URL = "https://www.90min.com/teams/arsenal"