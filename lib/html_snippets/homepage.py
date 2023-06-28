homepage_html = """
<main class="flex flex-col items-center overflow-hidden min-h-[calc(100vh-76px-50px)]" role="main" id="main-content">
          
    
    
    
    
    
    

    
    

    <section class="section min-h-[560px] flex-nowrap pt-[40px] babybear:flex-col babybear:min-h-[0] babybear:px-mobile-container-padding babybear:pt-[24px]" data-test-id="hero">
      <div class="self-start relative flex-shrink-0 w-[55%] pr-[42px] babybear:w-full babybear:pr-[0px]" data-test-id="hero__content">
        <h1 class="main-heading text-color-text-accent-2 babybear:pb-[24px]" data-test-id="hero__headline">
          Welcome to your professional community
        </h1>

<!---->
        
            <div class="hero-cta-form">
              
    
    
    
    
    
    
    
    
    
    

    
    
    
    

    
    <code id="i18n_username_error_empty" style="display: none"><!--"Please enter an email address or phone number"--></code>
    
    <code id="i18n_username_error_too_long" style="display: none"><!--"Email or phone number must be between 3 to 128 characters"--></code>
    <code id="i18n_username_error_too_short" style="display: none"><!--"Email or phone number must be between 3 to 128 characters"--></code>

    
    <code id="i18n_password_error_empty" style="display: none"><!--"Please enter a password"--></code>
    
    <code id="i18n_password_error_too_short" style="display: none"><!--"The password you provided must have at least 6 characters"--></code>
    
    <code id="i18n_password_error_too_long" style="display: none"><!--"The password you provided must have at most 400 characters"--></code>

    <form data-id="sign-in-form" action="https://www.linkedin.com/uas/login-submit" method="post" novalidate="" data-js-module-id="d2l-sign-in-form">
      <input name="loginCsrfParam" value="9b937b4e-5067-45d2-87a8-884153ea86e8" type="hidden">

      <div class="flex flex-col">
        
    <div class="mt-1.5" data-js-module-id="guest-input">
      <div class="flex flex-col">
        <label class="input-label mb-1" for="session_key">
          Email or phone
        </label>
        <div class="text-input flex">
          <input class="text-color-text font-sans text-md outline-0 bg-color-transparent grow" autocomplete="username" id="session_key" name="session_key" required="" type="text">
          
        </div>
      </div>

      <p class="input-helper mt-1.5" for="session_key" role="alert" data-js-module-id="guest-input__message"></p>
    </div>
  

        
    <div class="mt-1.5" data-js-module-id="guest-input">
      <div class="flex flex-col">
        <label class="input-label mb-1" for="session_password">
          Password
        </label>
        <div class="text-input flex">
          <input class="text-color-text font-sans text-md outline-0 bg-color-transparent grow" autocomplete="current-password" id="session_password" name="session_password" required="" type="password">
          
            <button aria-live="assertive" data-id="sign-in-form__password-visibility-toggle" class="font-sans text-md font-bold text-color-action z-10 ml-[12px] hover:cursor-pointer" aria-label="Show your LinkedIn password" data-tracking-control-name="homepage-basic_sign-in-password-visibility-toggle-btn" type="button">Show</button>
          
        </div>
      </div>

      <p class="input-helper mt-1.5" for="session_password" role="alert" data-js-module-id="guest-input__message"></p>
    </div>
  

        <input name="session_redirect" type="hidden">

<!---->      </div>

      <div data-id="sign-in-form__footer" class="flex justify-between
          sign-in-form__footer--full-width">
        <a data-id="sign-in-form__forgot-password" class="font-sans text-md font-bold link leading-regular
            sign-in-form__forgot-password--full-width" href="https://www.linkedin.com/uas/request-password-reset?trk=homepage-basic_forgot_password" data-tracking-control-name="homepage-basic_forgot_password" data-tracking-will-navigate="">Forgot password?</a>

<!---->
        <input name="trk" value="homepage-basic_sign-in-submit" type="hidden">
        <button class="btn-md btn-primary flex-shrink-0 cursor-pointer
            sign-in-form__submit-btn--full-width" data-id="sign-in-form__submit-btn" data-tracking-control-name="homepage-basic_sign-in-submit-btn" data-tracking-litms="" type="submit">
          Sign in
        </button>
      </div>
        <div class="sign-in-form__divider left-right-divider pt-2 pb-3">
          <p class="sign-in-form__divider-text font-sans text-sm text-color-text px-2">
            or
          </p>
        </div>
    <input type="hidden" name="controlId" value="d_homepage-guest-home-homepage-basic_sign-in-submit-btn"><input type="hidden" name="pageInstance" value="urn:li:page:d_homepage-guest-home_jsbeacon;xS2KWmtVTBijRy/ueLGEOQ=="></form>
      
    

    <form class="google-sign-in-cta-widget" action="https://www.linkedin.com/uas/login-submit" method="post" novalidate="">
      <input name="loginCsrfParam" value="9b937b4e-5067-45d2-87a8-884153ea86e8" type="hidden">

<!---->
      <input name="trk" value="homepage-basic_google-sign-in-submit" type="hidden">
      <button class="google-sign-in-cta-widget__btn btn-md btn-secondary hover:cursor-pointer flex items-center justify-center w-full h-auto" data-tracking-control-name="homepage-basic_google-sign-in-btn" data-tracking-litms="" type="button">
        <icon class="google-sign-in-cta-widget__icon onload w-[18px] min-h-[18px] leading-[18px] block lazy-loaded" aria-hidden="true" aria-busy="false"><svg xmlns="http://www.w3.org/2000/svg" id="Layer_1" data-name="Layer 1" viewBox="0 0 18 18" focusable="false" class="lazy-loaded" aria-busy="false"><defs><style>.cls-1{fill:#e94435;}.cls-1,.cls-2,.cls-3,.cls-4{fill-rule:evenodd;}.cls-2{fill:#f8bb15;}.cls-3{fill:#34a751;}.cls-4{fill:#547dbe;}</style></defs><title>Google</title><path class="cls-1" d="M9.12,3.37A5.41,5.41,0,0,1,13,4.8l2.39-2.39A8.79,8.79,0,0,0,9.12,0,9.08,9.08,0,0,0,1.05,4.77L3.78,6.93A5.62,5.62,0,0,1,9.12,3.37Z"></path><path class="cls-2" d="M3.39,9a5.63,5.63,0,0,1,.39-2.06L1.05,4.77A9,9,0,0,0,0,9a9.24,9.24,0,0,0,1,4.26l2.76-2.18A5.62,5.62,0,0,1,3.39,9Z"></path><path class="cls-3" d="M12.43,13.78A6.64,6.64,0,0,1,9,14.61a5.52,5.52,0,0,1-5.23-3.54L1,13.25A8.87,8.87,0,0,0,9,18a9.11,9.11,0,0,0,6.1-2.1Z"></path><path class="cls-4" d="M18,9a8.84,8.84,0,0,0-.18-1.79H9v3.6h5.46l0,.22a4.11,4.11,0,0,1-2,2.76l2.68,2.12A8.87,8.87,0,0,0,18,9Z"></path></svg></icon>
        <span class="google-sign-in-cta-widget__text ml-2">Sign in with Google</span>
      </button>

      
    <div class="loader loader--full-screen">
      <div class="loader__container mb-2 overflow-hidden">
        <icon class="loader__icon inline-block loader__icon--default text-color-progress-loading lazy-loaded" data-svg-class-name="loader__icon-svg--large fill-currentColor h-[60px] min-h-[60px] w-[60px] min-w-[60px]" aria-hidden="true" aria-busy="false"><svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 60 60" width="60" height="60" focusable="false" class="loader__icon-svg--large fill-currentColor h-[60px] min-h-[60px] w-[60px] min-w-[60px] lazy-loaded" aria-busy="false">
  <g>
    <path opacity="1" d="M30.1,16.1L30.1,16.1c-0.6,0-1-0.5-1-1V1c0-0.6,0.5-1,1-1l0,0c0.6,0,1,0.5,1,1v14.1C31.1,15.7,30.6,16.1,30.1,16.1z"></path>
    <path opacity="0.85" d="M23.1,18.1L23.1,18.1c-0.5,0.3-1.1,0.1-1.4-0.4L14.5,5.6c-0.3-0.5-0.2-1.1,0.4-1.4l0,0C15.4,3.9,16,4,16.3,4.6l7.2,12.1C23.8,17.2,23.6,17.8,23.1,18.1z"></path>
    <path opacity="0.77" d="M17.9,23.1L17.9,23.1c-0.3,0.5-0.9,0.7-1.4,0.4l-12.2-7c-0.5-0.3-0.7-0.9-0.4-1.4l0,0c0.3-0.5,0.9-0.7,1.4-0.4l12.2,7C18,22,18.2,22.7,17.9,23.1z"></path>
    <path opacity="0.69" d="M16.1,30.1L16.1,30.1c0,0.6-0.5,1-1,1L1,31.2c-0.6,0-1-0.5-1-1l0,0c0-0.6,0.5-1,1-1l14.1-0.1C15.7,29.1,16.1,29.5,16.1,30.1z"></path>
    <path opacity="0.61" d="M18,36.9L18,36.9c0.3,0.5,0.2,1.1-0.4,1.4L5.5,45.6c-0.5,0.3-1.1,0.2-1.4-0.4l0,0c-0.3-0.5-0.2-1.1,0.4-1.4l12.1-7.3C17.1,36.2,17.7,36.4,18,36.9z"></path>
    <path opacity="0.53" d="M23.3,42.1L23.3,42.1c0.5,0.3,0.6,0.9,0.4,1.4l-7.3,12.1c-0.3,0.5-0.9,0.6-1.4,0.4l0,0c-0.5-0.3-0.6-0.9-0.4-1.4l7.3-12.1C22.1,41.9,22.8,41.8,23.3,42.1z"></path>
    <path opacity="0.45" d="M30.1,43.9L30.1,43.9c0.6,0,1,0.5,1,1V59c0,0.6-0.5,1-1,1l0,0c-0.6,0-1-0.5-1-1V44.9C29,44.4,29.5,43.9,30.1,43.9z"></path>
    <path opacity="0.37" d="M37,41.9L37,41.9c0.5-0.3,1.1-0.2,1.4,0.4l7.2,12.1c0.3,0.5,0.2,1.1-0.4,1.4l0,0c-0.5,0.3-1.1,0.2-1.4-0.4l-7.2-12.1C36.4,42.8,36.6,42.2,37,41.9z"></path>
    <path opacity="0.29" d="M42.2,36.8L42.2,36.8c0.3-0.5,0.9-0.7,1.4-0.4l12.2,7c0.5,0.3,0.7,0.9,0.4,1.4l0,0c-0.3,0.5-0.9,0.7-1.4,0.4l-12.2-7C42.1,38,41.9,37.4,42.2,36.8z"></path>
    <path opacity="0.21 " d="M44,29.9L44,29.9c0-0.6,0.5-1,1-1h14.1c0.6,0,1,0.5,1,1l0,0c0,0.6-0.5,1-1,1L45,31C44.4,31,44,30.5,44,29.9z"></path>
    <path opacity="0.13" d="M42.1,23.1L42.1,23.1c-0.3-0.5-0.2-1.1,0.4-1.4l12.1-7.3c0.5-0.3,1.1-0.2,1.4,0.4l0,0c0.3,0.4,0.1,1.1-0.4,1.3l-12.1,7.3C43.1,23.7,42.4,23.6,42.1,23.1z"></path>
    <path opacity="0.05" d="M36.9,17.9L36.9,17.9c-0.5-0.3-0.6-0.9-0.4-1.4l7.3-12.1c0.3-0.5,0.9-0.6,1.4-0.4l0,0c0.5,0.3,0.6,0.9,0.4,1.4l-7.4,12.2C38,18.1,37.3,18.2,36.9,17.9z"></path>
    <animateTransform attributeName="transform" attributeType="XML" type="rotate" begin="0s" dur="1s" repeatCount="indefinite" calcMode="discrete" keyTimes="0;.0833;.166;.25;.3333;.4166;.5;.5833;.6666;.75;.8333;.9166;1" values="0,30,30;30,30,30;60,30,30;90,30,30;120,30,30;150,30,30;180,30,30;210,30,30;240,30,30;270,30,30;300,30,30;330,30,30;360,30,30"></animateTransform>
  </g>
</svg></icon>
      </div>
    </div>
  
    <input type="hidden" name="controlId" value="d_homepage-guest-home-homepage-basic_google-sign-in-btn"><input type="hidden" name="pageInstance" value="urn:li:page:d_homepage-guest-home_jsbeacon;xS2KWmtVTBijRy/ueLGEOQ=="><input type="hidden" name="controlId" value="d_homepage-guest-home-homepage-basic_google-sign-in-btn"><input type="hidden" name="pageInstance" value="urn:li:page:d_homepage-guest-home_jsbeacon;xS2KWmtVTBijRy/ueLGEOQ=="></form>
  
    <!---->  
            </div>
            <a class="sign-in-form__join-cta btn-md btn-secondary w-column babybear:w-full block mb-3" href="https://www.linkedin.com/signup" data-test-id="sign-in-join-cta" data-tracking-control-name="homepage-basic_sign-in-form_join-cta" data-tracking-will-navigate="">
              New to LinkedIn? Join now
            </a>
      
      </div>
        <img class="flip-rtl block z-[-1] w-[700px] h-[560px] relative flex-shrink babybear:w-[374px] babybear:h-[214px] babybear:static" alt="Welcome to your professional community" data-test-id="hero__illustration" src="https://static.licdn.com/aero-v1/sc/h/dxf91zhqd2z6b0bwg85ktm5s4">
    </section>
  
  
<!---->              
    
    
    
    
    <section class="section py-section flex-wrap babybear:flex-col papabear:flex-nowrap explore-content-hub" data-test-id="explore-content">
      <div class="self-start mb-[24px] w-full flex-shrink-0 papabear:w-column papabear:mr-[72px] papabear:mb-[0px]" data-test-id="pill-list-module__cta">
        <h2 class="secondary-heading">
          Explore collaborative articles
        </h2>
            
        <p class="font-extralight etta-text mt-[12px]">
          We’re unlocking community knowledge in a new way. Experts add insights directly into each article, started with the help of AI.
        </p>
      
          
        
      </div>

        <div class="w-full papabear:max-w-[calc(theme('spacing.content-max-w')-theme('spacing.column')-72px)]">
          
    
    
    
    

<!---->
    
    
    

      <ul class="show-more-less__list show-more-less__list--no-hidden-elems">
        
        
              
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/marketing-s2461/">
          
              Marketing
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/agriculture-s1197/">
          
              Agriculture
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/public-administration-s3697/">
          
              Public Administration
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/healthcare-s282/">
          
              Healthcare
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/engineering-s166/">
          
              Engineering
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/it-services-s57547/">
          
              IT Services
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/sustainability-s932/">
          
              Sustainability
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/business-administration-s50111/">
          
              Business Administration
            
        </a>
  
          </li>
          <li class="explore-content__pill">
            
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/telecommunications-s314/">
          
              Telecommunications
            
        </a>
  
          </li>
        <li class="explore-content__pill">
          
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary-emphasis" data-tracking-control-name="homepage-basic_explore-content_topic-pill" data-tracking-will-navigate="" href="https://www.linkedin.com/pulse/topics/home/">
          
            Show all
          
        </a>
  
        </li>
      
            
      
      </ul>
  
  
        </div>
    </section>
  
  
<!---->            
    
    

    
    <section class="section py-section flex-wrap babybear:flex-col papabear:flex-nowrap" data-test-id="search-cta">
      <div class="self-start mb-[24px] w-full flex-shrink-0 papabear:w-column papabear:mr-[72px] papabear:mb-[0px]" data-test-id="pill-list-module__cta">
        <h2 class="secondary-heading">
          Find the right job or internship for you
        </h2>
<!---->
        
      </div>

        <div class="w-full papabear:max-w-[calc(theme('spacing.content-max-w')-theme('spacing.column')-72px)]">
          
    
    
    
    

      <h2 class="etta-caps-header mb-[20px]">
          Suggested Searches
      </h2>

    
    
    

      <div class="show-more-less etta-show-more-less">
<!---->
        <ul data-max-num-to-show="10" class="show-more-less__list show-more-less__list--hide-after-10" data-impression-id="homepage-basic_pill-list-module_etta-show-more-less_show-more-less">
          
        
              
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/engineering-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Engineering
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/business-development-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Business Development
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/finance-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Finance
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/administrative-assistant-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Administrative Assistant
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/retail-associate-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Retail Associate
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/customer-service-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Customer Service
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/operations-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Operations
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/information-technology-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Information Technology
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/marketing-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Marketing
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/human-resources-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Human Resources
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/healthcare-services-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Healthcare Service
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/sales-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Sales
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/program-and-project-management-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Program and Project Management
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/accounting-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Accounting
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/arts-and-design-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Arts and Design
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/community-and-social-services-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Community and Social Services
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/consulting-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Consulting
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/education-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Education
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/entrepreneurship-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Entrepreneurship
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/legal-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Legal
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/media-and-communications-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Media and Communications
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/military-and-protective-services-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Military and Protective Services
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/product-management-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Product Management
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/purchasing-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Purchasing
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/quality-assurance-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Quality Assurance
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/real-estate-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Real Estate
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/research-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Research
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/support-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Support
        
        </a>
  
      </li>
      <li>
        
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic_suggested-search" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/administrative-jobs-etna-wy?trk=homepage-basic_suggested-search">
          
          Administrative
        
        </a>
  
      </li>
  
      
            
      
        </ul>

            <button class="show-more-less__button show-more-less__more-button show-more-less-button
                " aria-expanded="false" aria-label="Show more Suggested Searches" data-tracking-control-name="homepage-basic_pill-list-module_etta-show-more-less_show_more">
                Show more
              <icon class="show-more-less__button--chevron show-more-less-button-icon" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/cyolgscd0imw2ldqppkrb84vo"></icon>
            </button>

            <button class="show-more-less__button show-more-less__less-button show-more-less-button
                show-more-less__button--hide" aria-expanded="false" aria-label="Show less Suggested Searches" data-tracking-control-name="homepage-basic_pill-list-module_etta-show-more-less_show_more">
                Show less
              <icon class="show-more-less__button--chevron show-more-less-button-icon lazy-loaded" aria-hidden="true" aria-busy="false"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" preserveAspectRatio="xMinYMin meet" focusable="false" class="lazy-loaded" aria-busy="false"><path d="M8 7l-5.9 4L1 9.5l6.2-4.2c.5-.3 1.2-.3 1.7 0L15 9.5 13.9 11 8 7z" fill="currentColor"></path></svg></icon>
            </button>
      </div>
  
  
        </div>
    </section>
  
  
              <section class="section">
                
    
    

    <div class="w-full flex flex-row items-center py-[70px] after:full-color-bkg after:content-[''] after:bg-[#f1ece5] babybear:flex-col babybear:items-start babybear:py-[56px] babybear:px-mobile-container-padding" data-impression-id="homepage-basic_talent-finder-cta" data-test-id="talent-finder-cta">
      <h2 class="tertiary-heading w-talent-finder-header babybear:mb-[24px] babybear:w-unset">
        Post your job for millions of people to see
      </h2>
      
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary-emphasis flex-shrink babybear:my-auto babybear:mx-[0px]" data-tracking-control-name="homepage-basic_talent-finder-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/talent/post-a-job?trk=homepage-basic_talent-finder-cta">
          
        Post a job
      
        </a>
  
    </div>
  
              </section>
            

    
    

    
    

    
    

    <div data-nosnippet="" class="section min-h-section py-section after:full-color-bkg after:content-[''] after:bg-color-background-canvas babybear:mx-[-16px] babybear:pt-[0px]">
      

    
    
    
    
    
    

    <section class="slide-list relative  w-full">
      <header class="slide-list__header mb-1.5">
<!---->      </header>


          <div class="slide-list__nav">
            <div class="slide-list__nav-wrap absolute flex h-full items-center top-0 z-1 slide-list__nav-wrap--prev left-[-20px]">
              <div class="previous-slide-list__a11y-notification sr-only hidden" role="alert">
                No more previous content
              </div>
              <button data-tracking-control-name="homepage-basic_testimonials_slide_list_prev_button" class="slide-list__nav-button btn-sm btn-overlay cursor-pointer disabled:hidden" aria-label="Previous Slide" data-direction="prev" disabled="">
                <icon class="slide-list__nav-icon flex items-center justify-center pointer-events-none h-3 rtl:-scale-x-100 rtl:translate-x-[7px] lazy-loaded" aria-hidden="true" aria-busy="false"><svg xmlns="http://www.w3.org/2000/svg" width="7" height="14" viewBox="0 0 7 14" fill="none" focusable="false" class="lazy-loaded" aria-busy="false">
<path d="M4.6 0L0 7L4.6 14H7L2.4 7L7 0H4.6Z" style="fill: currentColor"></path>
</svg></icon>
              </button>
            </div>
          </div>

        <div class="relative overflow-hidden">
              <ul class="slide-list__list items-stretch flex list-none transition-all duration-slow ease-standard " style="transform: translate3d(0px, 0px, 0px);">
                
          
  <li class="flex justify-between relative items-center mr-[96px] w-full babybear:flex babybear:flex-wrap-reverse babybear:mr-[16px]" data-test-id="testimonial">
    <div class="w-[564px] mr-[64px] mamabear:max-w-[50vw] babybear:w-[300px] babybear:mt-[16px] babybear:mr-[0]">
      <h2 class="font-sans text-[40px] leading-[1.25] text-color-text-accent-2 babybear:text-[24px]">
        Let the right people know you’re open to work
      </h2>
      <p class="font-sans text-[32px] font-extralight text-black-a90 leading-[1.25] my-[8px] babybear:text-[18px]">
        <span>With the Open To Work feature, you can privately tell recruiters or publicly share with the LinkedIn community that you are looking for new job opportunities.</span>
      </p>
    </div>
    <img class="w-[450px] rounded-[50%] mamabear:max-w-[50vw] babybear:h-[300px] babybear:w-[300px] babybear:mt-[16px] babybear:mx-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/dbvmk0tsk0o0hd59fi64z3own" alt="">
  </li>

          
  <li class="flex justify-between relative items-center mr-[96px] w-full babybear:flex babybear:flex-wrap-reverse babybear:mr-[16px]" data-test-id="testimonial" aria-hidden="true">
    <div class="w-[564px] mr-[64px] mamabear:max-w-[50vw] babybear:w-[300px] babybear:mt-[16px] babybear:mr-[0]">
      <h2 class="font-sans text-[40px] leading-[1.25] text-color-text-accent-2 babybear:text-[24px]">
        Conversations today could lead to opportunity tomorrow
      </h2>
      <p class="font-sans text-[32px] font-extralight text-black-a90 leading-[1.25] my-[8px] babybear:text-[18px]">
        <span>Sending messages to people you know is a great way to strengthen relationships as you take the next step in your career.</span>
      </p>
    </div>
    <img class="w-[450px] rounded-[50%] mamabear:max-w-[50vw] babybear:h-[300px] babybear:w-[300px] babybear:mt-[16px] babybear:mx-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/2r8kd5zqpi905lkzsshdlvvn5" alt="">
  </li>

          
  <li class="flex justify-between relative items-center mr-[96px] w-full babybear:flex babybear:flex-wrap-reverse babybear:mr-[16px]" data-test-id="testimonial" aria-hidden="true">
    <div class="w-[564px] mr-[64px] mamabear:max-w-[50vw] babybear:w-[300px] babybear:mt-[16px] babybear:mr-[0]">
      <h2 class="font-sans text-[40px] leading-[1.25] text-color-text-accent-2 babybear:text-[24px]">
        Stay up to date on your industry
      </h2>
      <p class="font-sans text-[32px] font-extralight text-black-a90 leading-[1.25] my-[8px] babybear:text-[18px]">
        <span>From live videos, to stories, to newsletters and more, LinkedIn is full of ways to stay up to date on the latest discussions in your industry.</span>
      </p>
    </div>
    <img class="w-[450px] rounded-[50%] mamabear:max-w-[50vw] babybear:h-[300px] babybear:w-[300px] babybear:mt-[16px] babybear:mx-auto" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/ann24vsq7r0ux3vipqa1n90gg" alt="">
  </li>

      
              </ul>
        </div>

          <div class="slide-list__nav">
            <div class="slide-list__nav-wrap absolute flex h-full items-center top-0 z-1 slide-list__nav-wrap--next right-[-20px]">
              <div class="next-slide-list__a11y-notification sr-only hidden" role="alert">
                No more next content
              </div>
              <button data-tracking-control-name="homepage-basic_testimonials_slide_list_next_button" class="slide-list__nav-button btn-sm btn-overlay cursor-pointer disabled:hidden" aria-label="Next Slide" data-direction="next">
                <icon class="slide-list__nav-icon flex items-center justify-center pointer-events-none h-3 rtl:-scale-x-100 rtl:translate-x-[7px]" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/c9dcz2pyrbwi3sr6xwxigmvlz"></icon>
              </button>
            </div>
          </div>


<!---->    </section>
  
    </div>
  
<!---->            <section class="section py-section">
              
    
    
    
    <div class="flex flex-row flex-wrap justify-between w-full babybear:flex-column mamabear:py-[60px] mamabear:px-[0px] papabear:py-[60px] papabear:px-[0px]" data-test-id="product-cta">
      
    <section class="tile-module section py-section flex-wrap">
      
    <div class="flex flex-grow mr-[16px] self-start flex-col last:mr-0">
      <img class="flex-shrink-0 h-[312px] mr-[72px] mb-[16px] w-[312px] babybear:h-[240px] babybear:w-[240px]" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/b1fxwht7hdbeusleja7ciftsj" alt="">
      <div class="max-w-[456px] my-auto babybear:w-full">
        <h2 class="secondary-heading">
          Connect with people who can help
        </h2>

<!---->
          <div class="mt-[40px] babybear:mt-[24px]">
            
          
          
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-secondary" data-tracking-control-name="homepage-basic" data-tracking-will-navigate="" href="https://www.linkedin.com/pub/dir/+/+?trk=homepage-basic">
          
            Find people you know
          
        </a>
  
        
        
          </div>
      </div>
    </div>
  

        
    <div class="flex flex-grow mr-[16px] self-start flex-col last:mr-0">
      <img class="flex-shrink-0 h-[312px] mr-[72px] mb-[16px] w-[312px] babybear:h-[240px] babybear:w-[240px]" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/dkfub4sc7jgzg3o31flfr91rv" alt="">
      <div class="max-w-[456px] my-auto babybear:w-full">
        <h2 class="secondary-heading">
          Learn the skills you need to succeed
        </h2>

<!---->
          <div class="mt-[40px] babybear:mt-[24px]">
            
            
          
    
    
    
      
    <div class="dropdown-to-modal learning-cta__dropdown-modal">
        

    

    <div class="collapsible-dropdown flex items-center relative hyphens-auto">
          
            
          <button class="dropdown-to-modal__button collapsible-dropdown__button btn-md btn-tertiary cursor-pointer
              bg-white flex h-auto items-center justify-between w-[360px] py-[16px] pr-[12px] pl-[16px] border-[1px] border-solid border-black-a16 rounded-[5px] hover:text-black-a90 babybear:w-full" aria-expanded="false" data-tracking-control-name="homepage-basic_learning-cta">
            <span class="font-sans font-regular text-[20px] text-black-a90 leading-regular">Choose a topic to learn about</span>
            <icon aria-hidden="true" class="w-[24px] h-[24px] ml-[8px]" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/7asbl4deqijhoy3z2ivveispv"></icon>
          </button>
        
          

        <div class="collapsible-dropdown__list hidden container-raised absolute w-auto overflow-y-auto flex-col items-stretch z-1 bottom-auto top-[100%]" tabindex="-1">
          
            
          <ul class="w-[358px] overflow-scroll mt-[4px] pb-[16px]
              max-h-[380px]">
              <li aria-label="Business Analysis and Strategy 900+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/business-analysis-and-strategy?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Business Analysis and Strategy</span>
                    <span class="etta-dropdown-subtext">
                      900+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Business Software and Tools 1,960+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/business-software-and-tools?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Business Software and Tools</span>
                    <span class="etta-dropdown-subtext">
                      1,960+ course
                    </span>
                </a>
              </li>
              <li aria-label="Career Development 490+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/career-development-5?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Career Development</span>
                    <span class="etta-dropdown-subtext">
                      490+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Customer Service 190+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/customer-service-3?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Customer Service</span>
                    <span class="etta-dropdown-subtext">
                      190+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Diversity, Equity, and Inclusion (DEI) 230+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/diversity-equity-and-inclusion-dei?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Diversity, Equity, and Inclusion (DEI)</span>
                    <span class="etta-dropdown-subtext">
                      230+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Finance and Accounting 280+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/finance-and-accounting?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Finance and Accounting</span>
                    <span class="etta-dropdown-subtext">
                      280+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Human Resources 390+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/human-resources-3?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Human Resources</span>
                    <span class="etta-dropdown-subtext">
                      390+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Leadership and Management 1,450+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/leadership-and-management?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Leadership and Management</span>
                    <span class="etta-dropdown-subtext">
                      1,450+ course
                    </span>
                </a>
              </li>
              <li aria-label="Marketing 860+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/marketing-2?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Marketing</span>
                    <span class="etta-dropdown-subtext">
                      860+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Professional Development 1,420+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/professional-development?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Professional Development</span>
                    <span class="etta-dropdown-subtext">
                      1,420+ course
                    </span>
                </a>
              </li>
              <li aria-label="Project Management 420+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/project-management?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Project Management</span>
                    <span class="etta-dropdown-subtext">
                      420+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Sales 250+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/sales-3?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Sales</span>
                    <span class="etta-dropdown-subtext">
                      250+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Small Business and Entrepreneurship 320+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/small-business-and-entrepreneurship?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Small Business and Entrepreneurship</span>
                    <span class="etta-dropdown-subtext">
                      320+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Training and Education 290+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/training-and-education?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Training and Education</span>
                    <span class="etta-dropdown-subtext">
                      290+ courses
                    </span>
                </a>
              </li>
              <li aria-label="AEC 1,420+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/aec?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">AEC</span>
                    <span class="etta-dropdown-subtext">
                      1,420+ course
                    </span>
                </a>
              </li>
              <li aria-label="Animation and Illustration 1,690+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/animation-and-illustration?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Animation and Illustration</span>
                    <span class="etta-dropdown-subtext">
                      1,690+ course
                    </span>
                </a>
              </li>
              <li aria-label="Audio and Music 410+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/audio-and-music?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Audio and Music</span>
                    <span class="etta-dropdown-subtext">
                      410+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Graphic Design 920+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/graphic-design?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Graphic Design</span>
                    <span class="etta-dropdown-subtext">
                      920+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Motion Graphics and VFX 900+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/motion-graphics-and-vfx?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Motion Graphics and VFX</span>
                    <span class="etta-dropdown-subtext">
                      900+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Photography 1,140+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/photography-2?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Photography</span>
                    <span class="etta-dropdown-subtext">
                      1,140+ course
                    </span>
                </a>
              </li>
              <li aria-label="Product and Manufacturing 1,420+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/product-and-manufacturing?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Product and Manufacturing</span>
                    <span class="etta-dropdown-subtext">
                      1,420+ course
                    </span>
                </a>
              </li>
              <li aria-label="User Experience 510+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/user-experience?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">User Experience</span>
                    <span class="etta-dropdown-subtext">
                      510+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Video 590+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/video-2?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Video</span>
                    <span class="etta-dropdown-subtext">
                      590+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Visualization and Real-Time 1,300+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/visualization-and-real-time?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Visualization and Real-Time</span>
                    <span class="etta-dropdown-subtext">
                      1,300+ course
                    </span>
                </a>
              </li>
              <li aria-label="Web Design 530+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/web-design?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Web Design</span>
                    <span class="etta-dropdown-subtext">
                      530+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Artificial Intelligence (AI) 240+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/artificial-intelligence?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Artificial Intelligence (AI)</span>
                    <span class="etta-dropdown-subtext">
                      240+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Cloud Computing 1,140+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/cloud-computing-5?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Cloud Computing</span>
                    <span class="etta-dropdown-subtext">
                      1,140+ course
                    </span>
                </a>
              </li>
              <li aria-label="Data Science 880+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/data-science?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Data Science</span>
                    <span class="etta-dropdown-subtext">
                      880+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Database Management 360+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/database-management?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Database Management</span>
                    <span class="etta-dropdown-subtext">
                      360+ courses
                    </span>
                </a>
              </li>
              <li aria-label="DevOps 270+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/devops?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">DevOps</span>
                    <span class="etta-dropdown-subtext">
                      270+ courses
                    </span>
                </a>
              </li>
              <li aria-label="IT Help Desk 330+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/it-help-desk-5?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">IT Help Desk</span>
                    <span class="etta-dropdown-subtext">
                      330+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Mobile Development 470+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/mobile-development?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Mobile Development</span>
                    <span class="etta-dropdown-subtext">
                      470+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Network and System Administration 1,340+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/network-and-system-administration?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Network and System Administration</span>
                    <span class="etta-dropdown-subtext">
                      1,340+ course
                    </span>
                </a>
              </li>
              <li aria-label="Security 720+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/security-3?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Security</span>
                    <span class="etta-dropdown-subtext">
                      720+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Software Development 2,170+ courses" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/software-development?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Software Development</span>
                    <span class="etta-dropdown-subtext">
                      2,170+ courses
                    </span>
                </a>
              </li>
              <li aria-label="Web Development 1,400+ course" class="mt-[16px] mr-[8px] mb-[0] ml-[16px]" role="menuitem">
                <a class="flex flex-col text-black-a90 hover:text-blue-70 hover:visited:text-blue-70" data-tracking-control-name="homepage-basic_learning-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/topics/web-development?trk=homepage-basic_learning-cta">
                  <span class="etta-dropdown-header">Web Development</span>
                    <span class="etta-dropdown-subtext">
                      1,400+ course
                    </span>
                </a>
              </li>
          </ul>
        
          
        </div>

<!---->    </div>
  
    </div>
  
  
        
          
          </div>
      </div>
    </div>
  
    </section>
  
    </div>
  
            </section>
            <section class="section min-h-section py-section">
              

    
    
    
    
    

    <div class="flex flex-row flex-nowrap h-[720px] w-full after:full-color-bkg after:content-[''] after:bg-color-background-canvas papabear:after:brand-discovery-bkg mamabear:after:brand-discovery-bkg babybear:h-full" data-impression-id="homepage-basic_brand-discovery" data-test-id="brand-discovery">
      

    
    
    

    <div class="flex flex-row flex-nowrap h-auto mb-hero-content babybear:w-full babybear:mb-[0px] !block min-w-[50%] w-[50%] my-auto pr-[50px] babybear:pr-[0px]" data-test-id="" data-impression-id="homepage-basic_brand-discovery_intent-module">
        
          <h2 class="tertiary-heading mb-[8px]">
            Who is LinkedIn for?
          </h2>
          <h3 class="etta-subtitle mb-[40px] babybear:mb-[24px]">
            Anyone looking to navigate their professional life.
          </h3>
        
      <ul class="w-full">
        
  <li class="mb-[16px]">
    <a class="etta-btn bg-color-background-canvas-mobile
              hover:text-color-text hover:bg-[#e1dad0]" data-tracking-control-name="homepage-basic_brand-discovery_intent-module-firstBtn" data-tracking-will-navigate="" href="https://www.linkedin.com/pub/dir/+/+?trk=homepage-basic_brand-discovery_intent-module-firstBtn">
      
          Find a coworker or classmate
        
      <icon aria-hidden="true" class="ml-[16px] flip-rtl" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/3l4csbmaa6sv4gtsledhbu9lq"></icon>
    </a>
  </li>

        
  <li class="mb-[16px]">
    <a class="etta-btn bg-color-background-canvas-mobile
              hover:text-color-text hover:bg-[#e1dad0]" data-tracking-control-name="homepage-basic_brand-discovery_intent-module-secondBtn" data-tracking-will-navigate="" href="https://www.linkedin.com/jobs/jobs-in-etna-wy?trk=homepage-basic_brand-discovery_intent-module-secondBtn">
      
          Find a new job
        
      <icon aria-hidden="true" class="ml-[16px] flip-rtl" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/3l4csbmaa6sv4gtsledhbu9lq"></icon>
    </a>
  </li>

        
  <li class="mb-[16px]">
    <a class="etta-btn bg-color-background-canvas-mobile
              hover:text-color-text hover:bg-[#e1dad0]" data-tracking-control-name="homepage-basic_brand-discovery_intent-module-thirdBtn" data-tracking-will-navigate="" href="https://www.linkedin.com/learning/search?trk=homepage-basic_brand-discovery_intent-module-thirdBtn">
      
          Find a course or training
        
      <icon aria-hidden="true" class="ml-[16px] flip-rtl" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/3l4csbmaa6sv4gtsledhbu9lq"></icon>
    </a>
  </li>

      </ul>
    </div>
  

        <img class="h-[840px] self-center ml-[96px] flip-rtl babybear:hidden" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/292yd0en6qdvkbezeuj71yu4y" alt="Who is LinkedIn for?">
    </div>
  
            </section>
<!---->          
    <section class="section min-h-section py-section">
      <div data-test-id="bottom-cta-section" class="w-full self-start lazy-load after-lazy-bg-join after:content-[''] after:full-color-bkg after:bg-repeat-x after:bg-bottom after:bg-full-y babybear:h-full babybear:p-[0] babybear:after:content-[none]">
        <h2 class="main-heading text-black-a90 mt-[48px] mb-[16px] keep-all babybear:mt-[0px] babybear:mb-[24px]" id="bottom-cta-section__header">
          Join your colleagues, classmates, and friends on LinkedIn.
        </h2>

<!---->
        
              
        <a class="btn-md mb-1.5 mr-[6px] flex items-center w-max float-left btn-primary" data-tracking-control-name="homepage-basic_join-cta" data-tracking-will-navigate="" href="https://www.linkedin.com/signup?trk=homepage-basic_join-cta" aria-describedby="bottom-cta-section__header">
          
                Get started
              
        </a>
  
            
      </div>
    </section>
  
          

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

    <section class="directory section w-full flex justify-between pt-[24px] pb-[22px] after:full-color-bkg after:content-[''] after:bg-color-background-canvas babybear:flex-col babybear:max-w-full babybear:py-[24px] babybear:px-mobile-container-padding" data-impression-id="homepage-basic_directory" data-test-id="directory-section">
      <icon class="self-start h-[21px] w-[84px] text-blue-70" data-delayed-url="https://static.licdn.com/aero-v1/sc/h/b0sinzszgdrksde0dzc0leckm"></icon>
      <div class="w-full flex justify-end pl-[16px] babybear:flex-col babybear:flex-wrap babybear:mt-[24px] babybear:pl-[0px]">
          <div class="w-full max-w-[192px] mr-3">
            <h3 class="font-sans text-[16px] font-bold text-black-a90 leading-[1.25] mb-1 babybear:max-w-full babybear:my-[10px]">
              General
            </h3>
            <ul>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/signup?trk=guest_homepage-basic_directory" data-tracking-control-name="guest_homepage-basic_directory" data-tracking-will-navigate="">
                      Sign Up
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/help/linkedin?lang=en&amp;trk=homepage-basic_directory_helpCenterUrl" data-tracking-control-name="homepage-basic_directory_helpCenterUrl" data-tracking-will-navigate="">
                      Help Center
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://about.linkedin.com/?trk=homepage-basic_directory_aboutUrl" data-tracking-control-name="homepage-basic_directory_aboutUrl" data-tracking-will-navigate="">
                      About
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://press.linkedin.com/?trk=homepage-basic_directory_pressMicrositeUrl" data-tracking-control-name="homepage-basic_directory_pressMicrositeUrl" data-tracking-will-navigate="">
                      Press
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://blog.linkedin.com/?trk=homepage-basic_directory_blogMicrositeUrl" data-tracking-control-name="homepage-basic_directory_blogMicrositeUrl" data-tracking-will-navigate="">
                      Blog
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/company/linkedin/jobs?trk=homepage-basic_directory_careersUrl" data-tracking-control-name="homepage-basic_directory_careersUrl" data-tracking-will-navigate="">
                      Careers
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://developer.linkedin.com/?trk=homepage-basic_directory_developerMicrositeUrl" data-tracking-control-name="homepage-basic_directory_developerMicrositeUrl" data-tracking-will-navigate="">
                      Developers
                    </a>
                  </li>
            </ul>
          </div>
          <div class="w-full max-w-[192px] mr-3">
            <h3 class="font-sans text-[16px] font-bold text-black-a90 leading-[1.25] mb-1 babybear:max-w-full babybear:my-[10px]">
              Browse LinkedIn
            </h3>
            <ul>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/learning/?trk=homepage-basic_directory_learningHomeUrl" data-tracking-control-name="homepage-basic_directory_learningHomeUrl" data-tracking-will-navigate="">
                      Learning
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/jobs?trk=homepage-basic_directory_jobsHomeUrl" data-tracking-control-name="homepage-basic_directory_jobsHomeUrl" data-tracking-will-navigate="">
                      Jobs
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/salary/?trk=homepage-basic_directory_salaryHomeUrl" data-tracking-control-name="homepage-basic_directory_salaryHomeUrl" data-tracking-will-navigate="">
                      Salary
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://mobile.linkedin.com/?trk=homepage-basic_directory_mobileMicrositeUrl" data-tracking-control-name="homepage-basic_directory_mobileMicrositeUrl" data-tracking-will-navigate="">
                      Mobile
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/services?trk=homepage-basic_directory_servicesHomeUrl" data-tracking-control-name="homepage-basic_directory_servicesHomeUrl" data-tracking-will-navigate="">
                      Services
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/products?trk=homepage-basic_directory_productsHomeUrl" data-tracking-control-name="homepage-basic_directory_productsHomeUrl" data-tracking-will-navigate="">
                      Products
                    </a>
                  </li>
            </ul>
          </div>
          <div class="w-full max-w-[192px] mr-3">
            <h3 class="font-sans text-[16px] font-bold text-black-a90 leading-[1.25] mb-1 babybear:max-w-full babybear:my-[10px]">
              Business Solutions
            </h3>
            <ul>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://business.linkedin.com/talent-solutions?src=li-footer&amp;utm_source=linkedin&amp;utm_medium=footer&amp;trk=homepage-basic_directory_talentSolutionsMicrositeUrl" data-tracking-control-name="homepage-basic_directory_talentSolutionsMicrositeUrl" data-tracking-will-navigate="">
                      Talent
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://business.linkedin.com/marketing-solutions?src=li-footer&amp;utm_source=linkedin&amp;utm_medium=footer&amp;trk=homepage-basic_directory_marketingSolutionsMicrositeUrl" data-tracking-control-name="homepage-basic_directory_marketingSolutionsMicrositeUrl" data-tracking-will-navigate="">
                      Marketing
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://business.linkedin.com/sales-solutions?src=li-footer&amp;utm_source=linkedin&amp;utm_medium=footer&amp;trk=homepage-basic_directory_salesSolutionsMicrositeUrl" data-tracking-control-name="homepage-basic_directory_salesSolutionsMicrositeUrl" data-tracking-will-navigate="">
                      Sales
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://learning.linkedin.com/?src=li-footer&amp;trk=homepage-basic_directory_learningMicrositeUrl" data-tracking-control-name="homepage-basic_directory_learningMicrositeUrl" data-tracking-will-navigate="">
                      Learning
                    </a>
                  </li>
            </ul>
          </div>
          <div class="w-full max-w-[192px] mr-3">
            <h3 class="font-sans text-[16px] font-bold text-black-a90 leading-[1.25] mb-1 babybear:max-w-full babybear:my-[10px]">
              Directories
            </h3>
            <ul>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/people?trk=homepage-basic_directory_peopleDirectoryUrl" data-tracking-control-name="homepage-basic_directory_peopleDirectoryUrl" data-tracking-will-navigate="">
                      Members
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/jobs?trk=homepage-basic_directory_jobSearchDirectoryUrl" data-tracking-control-name="homepage-basic_directory_jobSearchDirectoryUrl" data-tracking-will-navigate="">
                      Jobs
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/companies?trk=homepage-basic_directory_companyDirectoryUrl" data-tracking-control-name="homepage-basic_directory_companyDirectoryUrl" data-tracking-will-navigate="">
                      Companies
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/featured?trk=homepage-basic_directory_featuredDirectoryUrl" data-tracking-control-name="homepage-basic_directory_featuredDirectoryUrl" data-tracking-will-navigate="">
                      Featured
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/learning?trk=homepage-basic_directory_learningDirectoryUrl" data-tracking-control-name="homepage-basic_directory_learningDirectoryUrl" data-tracking-will-navigate="">
                      Learning
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/posts?trk=homepage-basic_directory_postsDirectoryUrl" data-tracking-control-name="homepage-basic_directory_postsDirectoryUrl" data-tracking-will-navigate="">
                      Posts
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/articles?trk=homepage-basic_directory_articlesDirectoryUrl" data-tracking-control-name="homepage-basic_directory_articlesDirectoryUrl" data-tracking-will-navigate="">
                      Articles
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/schools?trk=homepage-basic_directory_schoolsDirectoryUrl" data-tracking-control-name="homepage-basic_directory_schoolsDirectoryUrl" data-tracking-will-navigate="">
                      Schools
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/news?trk=homepage-basic_directory_newsDirectoryUrl" data-tracking-control-name="homepage-basic_directory_newsDirectoryUrl" data-tracking-will-navigate="">
                      News
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/newsletters?trk=homepage-basic_directory_newslettersDirectoryUrl" data-tracking-control-name="homepage-basic_directory_newslettersDirectoryUrl" data-tracking-will-navigate="">
                      News Letters
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/services?trk=homepage-basic_directory_servicesDirectoryUrl" data-tracking-control-name="homepage-basic_directory_servicesDirectoryUrl" data-tracking-will-navigate="">
                      Services
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/products?trk=homepage-basic_directory_productsDirectoryUrl" data-tracking-control-name="homepage-basic_directory_productsDirectoryUrl" data-tracking-will-navigate="">
                      Products
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/advice?trk=homepage-basic_directory_adviceDirectoryUrl" data-tracking-control-name="homepage-basic_directory_adviceDirectoryUrl" data-tracking-will-navigate="">
                      Advice
                    </a>
                  </li>
                  <li class="babybear:my-[10px] babybear:max-w-full">
                    <a class="font-sans text-[14px] text-black-a60 font-bold leading-[1.25] visited:text-black-a60 hover:visited:text-blue-70" href="https://www.linkedin.com/directory/people-search?trk=homepage-basic_directory_peopleSearchDirectoryUrl" data-tracking-control-name="homepage-basic_directory_peopleSearchDirectoryUrl" data-tracking-will-navigate="">
                      People Search
                    </a>
                  </li>
            </ul>
          </div>
      </div>
    </section>
  
        </main>
"""

