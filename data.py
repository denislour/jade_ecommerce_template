class data:

    shopInfo = {
        'phone': '8 800 799 99 99',
        'email': 'example@example.com',
        'address': 'St.&nbsp;Petersburg, Nevsky&nbsp;Prospect&nbsp;28',
        'openingHours': 'Daily 10:00\xe2\x80\x9322:00',
        'storeName': 'Store Name',
        'latitude': 59.9356728,
        'longitude': 30.3258604,
        }

    catalog = [{
        'name': 'Laptops & Tablets',
        'id': 'laptops-tablets',
        'href': 'category.html',
        'image': 'static/images/catalog/computers.svg',
        'quantity': 367,
        'items_': ['Laptops', 'Tablets', 'Peripherals', 'Keyboards',
                'Accessories'],
        }, {
        'name': 'Phones & Gadgets',
        'id': 'phones-gadgets',
        'href': 'category.html',
        'image': 'static/images/catalog/phones.svg',
        'quantity': 144,
        'items_': ['Smartphones', 'Mobile Phones', 'Smart watches',
                'Charging and batteries', 'Accessories'],
        }, {
        'name': 'TV & Video',
        'id': 'tv-video',
        'href': 'category.html',
        'image': 'static/images/catalog/tv.svg',
        'quantity': 58,
        'items_': [
            'TV',
            'Home Cinema',
            'Satellite & Cable TV',
            'Projectors',
            'DVD & Blu-ray',
            'Accessories',
            ],
        }, {
        'name': 'Games & Entertainment',
        'id': 'games-entertainment',
        'href': 'category.html',
        'image': 'static/images/catalog/games.svg',
        'quantity': 13,
        'items_': ['Gaming consoles', 'Games', 'Software',
                'Joysticks & gamepads', 'Accessories'],
        }, {
        'name': 'Photo',
        'id': 'photo',
        'href': 'category.html',
        'image': 'static/images/catalog/photo.svg',
        'quantity': 59,
        'items_': ['Cameras', 'Lenses', 'Accessories'],
        }]

    brands = [
        {'name': 'Apple', 'image': 'static/images/brands/apple.svg'},
        {'name': 'Samsung', 'image': 'static/images/brands/samsung.svg'},
        {'name': 'Sony', 'image': 'static/images/brands/sony.svg'},
        {'name': 'Microsoft', 'image': 'static/images/brands/microsoft.svg'},
        {'name': 'Intel', 'image': 'static/images/brands/intel.svg'},
        {'name': 'HP', 'image': 'static/images/brands/hp.svg'},
        {'name': 'LG', 'image': 'static/images/brands/lg.svg'},
        {'name': 'Lenovo', 'image': 'static/images/brands/lenovo.svg'},
        {'name': 'ASUS', 'image': 'static/images/brands/asus.svg'},
        {'name': 'Acer', 'image': 'static/images/brands/acer.svg'},
        {'name': 'Dell', 'image': 'static/images/brands/dell.svg'},
        {'name': 'Canon', 'image': 'static/images/brands/canon.svg'},
        ]

    toolbarMenu = [{'name': 'News', 'href': 'news.html'}, {'name': 'FAQ',
                'href': 'faq.html'}, {'name': 'Payment', 'href': '#'}]

    navbarMenu = [
        {'name': 'Catalog', 'href': 'catalog.html', 'items_': catalog},
        {'name': 'Brands', 'href': 'brands.html', 'items_': brands},
        {'name': 'Pages', 'href': '#', 'items_': [
            {'name': 'Catalog', 'href': 'catalog.html'},
            {'name': 'Category', 'href': 'category.html'},
            {'name': 'Subcategory', 'href': 'subcategory.html'},
            {'name': 'Product', 'href': 'product.html'},
            {'name': 'Cart', 'href': 'cart.html'},
            {'name': 'Checkout', 'href': 'checkout.html'},
            {'name': 'Compare', 'href': 'compare.html'},
            {'name': 'Brands', 'href': 'brands.html'},
            {'name': 'Compare', 'href': 'compare.html'},
            {'name': 'Account', 'href': 'account.html'},
            {'name': 'Favorites', 'href': 'favorites.html'},
            {'name': 'Personal', 'href': 'personal.html'},
            {'name': 'Settings', 'href': 'settings.html'},
            {'name': 'About', 'href': 'about.html'},
            {'name': 'Contacts', 'href': 'contacts.html'},
            {'name': 'Blog', 'href': 'blog.html'},
            {'name': 'News', 'href': 'news.html'},
            {'name': 'Article', 'href': 'article.html'},
            {'name': 'FAQ', 'href': 'faq.html'},
            {'name': 'Delivery', 'href': 'delivery.html'},
            {'name': '404', 'href': '404.html'},
            ]},
        {'name': 'Blog', 'href': 'blog.html'},
        {'name': 'About', 'href': 'about.html'},
        {'name': 'Contacts', 'href': 'contacts.html'},
        ]

    footerMenuLeft = [{'name': 'Catalog', 'href': 'catalog.html'},
                    {'name': 'Brands', 'href': 'brands.html'},
                    {'name': 'Delivery', 'href': 'delivery.html'},
                    {'name': 'FAQ', 'href': 'faq.html'},
                    {'name': 'Payment', 'href': '#'}]

    footerMenuRight = [{'name': 'About', 'href': 'about.html'},
                    {'name': 'Contacts', 'href': 'contacts.html'},
                    {'name': 'Blog', 'href': 'blog.html'},
                    {'name': 'News', 'href': 'news.html'}]

    socials = [{'name': 'Facebook', 'icon': 'facebook'}, {'name': 'Twitter'
            , 'icon': 'twitter'}, {'name': 'YouTube', 'icon': 'youtube'
            }, {'name': 'Instagram', 'icon': 'instagram'}]

    products = [
        {
            'id': 1,
            'name': 'Apple MacBook Pro 15" Touch Bar MPTU2LL/A 256GB (Silver)'
                ,
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/1/1-small.jpg',
                    'medium': 'static/images/products/1/1-medium.jpg',
                    'large': 'static/images/products/1/1-large.jpg'},
            'additionalImages': [{'small': 'static/images/products/1/1-add-1-small.jpg'
                                ,
                                'large': 'static/images/products/1/1-add-1-large.jpg'
                                },
                                {'small': 'static/images/products/1/1-add-2-small.jpg'
                                ,
                                'large': 'static/images/products/1/1-add-2-large.jpg'
                                },
                                {'small': 'static/images/products/1/1-add-3-small.jpg'
                                ,
                                'large': 'static/images/products/1/1-add-3-large.jpg'
                                },
                                {'small': 'static/images/products/1/1-add-4-small.jpg'
                                ,
                                'large': 'static/images/products/1/1-add-4-large.jpg'
                                }],
            'price': '$1599.00',
            'oldPrice': '$1899.00',
            'brand': {'name': 'Apple', 'image': 'static/images/brands/apple.svg',
                    'href': '#'},
            'variations': [{'name': 'Color',
                        'values': [{'name': 'Space Grey',
                        'value': '#aaaeb1'}, {'name': 'Silver',
                        'value': '#dddfde'}]}, {'name': 'SSD Storage',
                        'values': [{'name': '256 GB', 'value': '256 GB'
                        }, {'name': '512 GB', 'value': '512 GB'}]}],
            'specifications': [
                {'name': 'Performance', 'properties': {
                    'Processor': 'Intel&nbsp;Core i7&nbsp;Quad-Core',
                    'Base Clock Speed': '2.8&nbsp;GHz',
                    'Maximum Boost Speed': '3.8&nbsp;GHz',
                    'Total Installed Memory': '16&nbsp;GB',
                    'Memory Type': 'LPDDR3&nbsp;SDRAM',
                    'Memory Speed': '2133&nbsp;MHz',
                    'Onboard Memory': '16&nbsp;GB',
                    'Available Memory Slots': '\xe2\x80\x94',
                    'Graphics Type': 'Hybrid',
                    'GPU': 'AMD Radeon&nbsp;Pro 555 with 2&nbsp;GB&nbsp;GDDR5 VRAM,<br>Intel HD Graphics&nbsp;630'
                        ,
                    }},
                {'name': 'Display', 'properties': {
                    'Panel Type': 'IPS',
                    'Size': '15.4"',
                    'Aspect Ratio': '16:10',
                    'Native Resolution': '2880\xc3\x971800',
                    'Touchscreen': '\xe2\x80\x94',
                    'Finish': 'Glossy',
                    'Brightness': '500&nbsp;cd/m<sup>2</sup>',
                    }},
                {'name': 'Drives', 'properties': {
                    'Available Slots': '\xe2\x80\x94',
                    'Total Capacity': '256&nbsp;GB',
                    'Solid State Storage': '1 \xc3\x97 256&nbsp;GB&nbsp;Integrated PCIe'
                        ,
                    'Optical Drive': '\xe2\x80\x94',
                    }},
                {'name': 'Input/ Output Connectors', 'properties': {
                    'Ports': '4 \xc3\x97 Thunderbolt 3&nbsp;via USB Type-C'
                        ,
                    'Display': '4 \xc3\x97 DisplayPort&nbsp;via Type-C',
                    'Audio': '1 \xc3\x97 1/8" (3.5&nbsp;mm) Headphone Output,<br>2 \xc3\x97 Integrated Speaker,<br>3 \xc3\x97 Integrated Microphone'
                        ,
                    'Expansion Slots': '\xe2\x80\x94',
                    'Media Card Slots': '\xe2\x80\x94',
                    }},
                {'name': 'Communications', 'properties': {
                    'Network': '\xe2\x80\x94',
                    'Modem': '\xe2\x80\x94',
                    'Wi-Fi': '802.11ac; Dual-Band',
                    'Bluetooth': 'Bluetooth 4.2',
                    'Mobile Broadband': '\xe2\x80\x94',
                    'GPS': 'Not Specified by Manufacturer',
                    'NFC': 'Not Specified by Manufacturer',
                    'Webcam': 'User-Facing: 720p Video',
                    }},
                {'name': 'Battery', 'properties': {
                    'Battery Chemistry': 'Lithium-Ion Polymer',
                    'Watt Hours / Type': '76&nbsp;Wh&nbsp;Non-Removable',
                    'Maximum Runtime': '10&nbsp;Hours',
                    'Power Requirements': '100-240&nbsp;VAC, 50-60&nbsp;Hz'
                        ,
                    'Power Supply': '1 \xc3\x97 87&nbsp;W',
                    }},
                {'name': 'General', 'properties': {
                    'Operating System': 'macOS High Sierra',
                    'Security': 'Not specified',
                    'Keyboard': 'Keys: 64,<br>type: Standard Notebook Keyboard,<br>Features: Backlight'
                        ,
                    'Pointing Device': 'Force Touch Trackpad',
                    'Dimensions (W \xc3\x97 H \xc3\x97 D)': '13.8 \xc3\x97 0.6 \xc3\x97 9.5"&nbsp;/&nbsp;35.1 \xc3\x97 1.5 \xc3\x97 24.1&nbsp;cm'
                        ,
                    'Weight': '4.02&nbsp;lb&nbsp;/&nbsp;1.82&nbsp;kg',
                    }},
                {'name': 'Packaging Info',
                'properties': {'Package Weight': '7.55&nbsp;lb',
                'Box Dimensions (L \xc3\x97 W \xc3\x97 H)': '16.2 \xc3\x97 11.6 \xc3\x97 3.7"'
                }},
                ],
            'reviews': [{
                'author': 'Thomas Bruns',
                'date': 'May 21, 2018',
                'text': '<p>Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren, no sea takimata sanctus est Lorem ipsum dolor sit amet.</p>'
                    ,
                'likes': 14,
                'dislikes': 2,
                }, {
                'author': 'George Clanton',
                'date': 'May 24, 2018',
                'text': '<p>Nunc interdum odio non erat commodo lacinia. Aliquam nec tincidunt lorem. Nunc quis scelerisque nulla. Nam nulla ante, luctus non dignissim a, luctus quis sem. Curabitur consectetur porttitor leo. Donec molestie nisl vitae lorem porttitor vehicula. Etiam feugiat a magna ac dapibus. Donec vitae sollicitudin lectus.</p><p>Sed mollis ex tincidunt posuere blandit. Mauris sed tellus dolor. Suspendisse nibh mi, dignissim et molestie id, dictum in arcu. Duis sodales scelerisque quam, quis lobortis felis egestas eu. Sed nibh nulla, aliquet ac leo vel, rutrum dignissim metus. Sed non rhoncus ex. Curabitur accumsan porta lacus non viverra. Etiam feugiat sapien ut purus luctus, eu porttitor neque volutpat.</p>'
                    ,
                'likes': 5,
                'dislikes': 0,
                }],
            'questions': [{'question': 'Lorem ipsum dolor sit amet, consectetur adipiscing elit?'
                        ,
                        'answer': 'Vivamus imperdiet venenatis est. Phasellus vitae mauris imperdiet, condimentum eros vel, ullamcorper turpis. Maecenas sed libero quis orci egestas vehicula fermentum id diam.'
                        },
                        {'question': 'Nullam massa sem, mollis ut luctus at, tincidunt a lorem?'
                        ,
                        'answer': 'Aliquam sed dictum elit, quis consequat metus. Proin in mauris finibus urna lacinia laoreet sed id orci.'
                        },
                        {'question': 'Aliquam pretium diam et ullamcorper malesuada?'
                        ,
                        'answer': 'Praesent feugiat lectus faucibus tellus congue pharetra. In viverra vehicula pellentesque. Etiam consectetur ultricies magna at bibendum.'
                        },
                        {'question': 'Nulla fringilla sollicitudin mauris eu volutpat?'
                        ,
                        'answer': 'Mauris quis neque nec lectus aliquet malesuada. Nunc ullamcorper purus id gravida aliquam. Integer eget blandit urna.'
                        },
                        {'question': 'Nam luctus velit ante, id pulvinar nisl gravida eget?'
                        ,
                        'answer': 'Vestibulum gravida nisi tempor malesuada iaculis. Phasellus finibus, nisl quis pellentesque scelerisque, erat erat mollis massa, eu semper diam eros id risus. Cras vitae nisi porta.'
                        }],
            'isNotAvailable': False,
            'isOnSale': True,
            'isAddedToCart': True,
            'isAddedToFavorites': True,
            'isAddedToCompare': True,
            'statuses': ['top selling', 'trade-in'],
            'properties': {
                'Diagonal display': '15.4"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i7',
                'RAM': '16&nbsp;GB',
                'Video Card': 'AMD Radeon Pro 555',
                },
            },
        {
            'id': 2,
            'name': 'Apple MacBook 12" MNYN2LL/A 512GB (Rose Gold)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/2/2-small.jpg',
                    'medium': 'static/images/products/2/2-medium.jpg',
                    'large': 'static/images/products/2/2-large.jpg'},
            'additionalImages': [],
            'price': '$1549.00',
            'oldPrice': '',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': False,
            'isAddedToCart': True,
            'isAddedToFavorites': True,
            'isAddedToCompare': True,
            'statuses': ['new', 'trade-in'],
            'properties': {
                'Diagonal display': '12"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i5',
                'RAM': '8&nbsp;GB',
                'Video Card': 'Intel\xc2\xae HD Graphics 615',
                },
            },
        {
            'id': 3,
            'name': 'Lenovo IdeaPad YOGA 920-13IKB 80Y7001RRK (Copper)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/3/3-small.jpg',
                    'medium': 'static/images/products/3/3-medium.jpg',
                    'large': 'static/images/products/3/3-large.jpg'},
            'additionalImages': [],
            'price': '$1199.00',
            'oldPrice': '',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': False,
            'isAddedToCart': False,
            'isAddedToFavorites': True,
            'isAddedToCompare': False,
            'statuses': '',
            'properties': {
                'Diagonal display': '13.9"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i7 8550U',
                'RAM': '16&nbsp;GB',
                'Video Card': 'Intel\xc2\xae HD Graphics 620',
                },
            },
        {
            'id': 4,
            'name': 'ASUS Zenbook UX330UA-FC020T (Rose Gold)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/4/4-small.jpg',
                    'medium': 'static/images/products/4/4-medium.jpg',
                    'large': 'static/images/products/4/4-large.jpg'},
            'additionalImages': [],
            'price': '$749.00',
            'oldPrice': '',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': False,
            'isAddedToCart': False,
            'isAddedToFavorites': False,
            'isAddedToCompare': False,
            'statuses': ['top selling'],
            'properties': {
                'Diagonal display': '13.3"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i7-6500U',
                'RAM': '8&nbsp;GB',
                'Video Card': 'Intel\xc2\xae HD Graphics 520',
                },
            },
        {
            'id': 5,
            'name': 'Dell XPS 15 9560-8968 (Silver)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/5/5-small.jpg',
                    'medium': 'static/images/products/5/5-medium.jpg',
                    'large': 'static/images/products/5/5-large.jpg'},
            'additionalImages': [],
            'price': '$949.00',
            'oldPrice': '$999.00',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': True,
            'isAddedToCart': False,
            'isAddedToFavorites': False,
            'isAddedToCompare': False,
            'statuses': '',
            'properties': {
                'Diagonal display': '15.6"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i7 7700HQ',
                'RAM': '16&nbsp;GB',
                'Video Card': 'NVIDIA GeForce GTX 960M',
                },
            },
        {
            'id': 6,
            'name': 'Apple MacBook Air 13" MQD32LL/A 128GB (Silver)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/6/6-small.jpg',
                    'medium': 'static/images/products/6/6-medium.jpg',
                    'large': 'static/images/products/6/6-large.jpg'},
            'additionalImages': [],
            'price': '$849.00',
            'oldPrice': '',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': False,
            'isAddedToCart': False,
            'isAddedToFavorites': False,
            'isAddedToCompare': True,
            'statuses': ['trade-in'],
            'properties': {
                'Diagonal display': '13.3"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i5',
                'RAM': '8&nbsp;GB',
                'Video Card': 'Intel\xc2\xae HD Graphics 6000',
                },
            },
        {
            'id': 7,
            'name': 'Dell Inspiron 5378-2063 (Gray)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/7/7-small.jpg',
                    'medium': 'static/images/products/7/7-medium.jpg',
                    'large': 'static/images/products/7/7-large.jpg'},
            'additionalImages': [],
            'price': '$579.00',
            'oldPrice': '$599.00',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': True,
            'isAddedToCart': False,
            'isAddedToFavorites': False,
            'isAddedToCompare': False,
            'statuses': '',
            'properties': {
                'Diagonal display': '13.3"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i3-7100U',
                'RAM': '4&nbsp;GB',
                'HDD Capacity': '1&nbsp;TB',
                },
            },
        {
            'id': 8,
            'name': 'Lenovo Yoga 720-13IKB 80X60059RK (Silver)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': {'small': 'static/images/products/8/8-small.jpg',
                    'medium': 'static/images/products/8/8-medium.jpg',
                    'large': 'static/images/products/8/8-large.jpg'},
            'additionalImages': [],
            'price': '$1099.00',
            'oldPrice': '',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': False,
            'isOnSale': False,
            'isAddedToCart': False,
            'isAddedToFavorites': False,
            'isAddedToCompare': False,
            'statuses': ['new'],
            'properties': {
                'Diagonal display': '13.3"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i5-7200U',
                'RAM': '8&nbsp;GB',
                'Video Card': 'Intel\xc2\xae HD Graphics 620',
                },
            },
        {
            'id': 9,
            'name': 'Lenovo ThinkPad X380 Yoga 20LH000MUS (Black)',
            'type': 'Laptop',
            'href': 'product.html',
            'image': '',
            'additionalImages': [],
            'price': '$2239.00',
            'oldPrice': '',
            'brand': {},
            'variations': [],
            'specifications': [],
            'reviews': [],
            'questions': [],
            'isNotAvailable': True,
            'isOnSale': False,
            'isAddedToCart': False,
            'isAddedToFavorites': False,
            'isAddedToCompare': False,
            'statuses': '',
            'properties': {
                'Diagonal display': '13.3"',
                'CPU': 'Intel\xc2\xae&nbsp;Core\xe2\x84\xa2 i7 8550U',
                'RAM': '4&nbsp;GB',
                'Video Card': 'Intel\xc2\xae UHD Graphics 620',
                },
            },
        ]

    filters = [
        {
            'id': 1,
            'name': 'brand',
            'title': 'Brands',
            'isOpen': True,
            'items_': [
                {'id': 1, 'name': 'Acer', 'quantity': 177},
                {'id': 2, 'name': 'Apple', 'quantity': 18},
                {'id': 3, 'name': 'ASUS', 'quantity': 150},
                {'id': 4, 'name': 'Dell', 'quantity': 170},
                {'id': 5, 'name': 'HP', 'quantity': 498},
                {'id': 6, 'name': 'MSI', 'quantity': 54},
                {'id': 7, 'name': 'Samsung', 'quantity': 1},
                {'id': 8, 'name': 'Sony', 'quantity': 1},
                ],
            },
        {
            'id': 2,
            'name': 'type',
            'title': 'Type',
            'description': 'A small description for this property',
            'isOpen': True,
            'items_': [{'id': 1, 'name': 'Notebook', 'quantity': 150},
                    {'id': 2, 'name': 'Ultrabook', 'quantity': 18},
                    {'id': 3, 'name': 'Transformer', 'quantity': 6}],
            },
        {
            'id': 3,
            'name': 'screen-size',
            'title': 'Screen Size',
            'description': 'A small description for this property',
            'isOpen': False,
            'items_': [
                {'id': 1, 'name': '11.6" and smaller', 'quantity': 45},
                {'id': 2, 'name': '12" - 13.5"', 'quantity': 178},
                {'id': 3, 'name': '14" - 14.5"', 'quantity': 461},
                {'id': 4, 'name': '15" - 15.6"', 'quantity': 148},
                {'id': 5, 'name': '17" - 17.3"', 'quantity': 73},
                {'id': 6, 'name': '18.4" and larger', 'quantity': 54},
                ],
            },
        {
            'id': 3,
            'name': 'screen-resolution',
            'title': 'Screen Resolution',
            'description': 'A small description for this property',
            'isOpen': False,
            'items_': [
                {'id': 1, 'name': '3840\xc3\x972160', 'quantity': 12},
                {'id': 2, 'name': '3200\xc3\x971800"', 'quantity': 12},
                {'id': 3, 'name': '2880\xc3\x971800', 'quantity': 10},
                {'id': 4, 'name': '2560\xc3\x971600', 'quantity': 7},
                {'id': 5, 'name': '2560\xc3\x971440', 'quantity': 13},
                {'id': 6, 'name': '1920\xc3\x971080', 'quantity': 341},
                {'id': 7, 'name': '1600\xc3\x97900', 'quantity': 11},
                {'id': 8, 'name': '1440\xc3\x97900', 'quantity': 13},
                {'id': 9, 'name': '1366\xc3\x97768', 'quantity': 237},
                {'id': 10, 'name': '1024\xc3\x97600', 'quantity': 5},
                ],
            },
        {
            'id': 4,
            'name': 'cpu',
            'title': 'CPU',
            'description': 'A small description for this property',
            'isOpen': False,
            'items_': [
                {'id': 1, 'name': 'AMD A-series', 'quantity': 102},
                {'id': 2, 'name': 'AMD E-series', 'quantity': 21},
                {'id': 3, 'name': 'AMD FX', 'quantity': 1},
                {'id': 4, 'name': 'AMD Ryzen', 'quantity': 1},
                {'id': 5, 'name': 'Intel Atom', 'quantity': 8},
                {'id': 6, 'name': 'Intel Celeron', 'quantity': 38},
                {'id': 7, 'name': 'Intel Core M', 'quantity': 6},
                {'id': 8, 'name': 'Intel Core i3', 'quantity': 143},
                {'id': 9, 'name': 'Intel Core i5', 'quantity': 273},
                {'id': 10, 'name': 'Intel Core i7', 'quantity': 218},
                {'id': 11, 'name': 'Intel Xeon', 'quantity': 3},
                {'id': 12, 'name': 'Intel Pentium', 'quantity': 86},
                ],
            },
        {
            'id': 5,
            'name': 'ram',
            'title': 'RAM',
            'description': 'A small description for this property',
            'isOpen': False,
            'items_': [
                {'id': 1, 'name': '2 GB', 'quantity': 17},
                {'id': 2, 'name': '4 GB', 'quantity': 359},
                {'id': 3, 'name': '6 GB', 'quantity': 81},
                {'id': 4, 'name': '8 GB', 'quantity': 346},
                {'id': 5, 'name': '12 GB', 'quantity': 13},
                {'id': 6, 'name': '16 GB', 'quantity': 72},
                {'id': 7, 'name': '24 GB', 'quantity': 1},
                {'id': 8, 'name': '32 GB', 'quantity': 11},
                ],
            },
        ]

    compare = [
        {'name': 'Performance', 'properties': {
            'Processor': ['Intel&nbsp;Core i7&nbsp;Quad-Core',
                        'Intel&nbsp;Core i5&nbsp;Dual-Core',
                        'Intel&nbsp;Core i5&nbsp;Dual-Core'],
            'Base Clock Speed': ['2.8&nbsp;GHz', '1.3&nbsp;GHz',
                                '1.8&nbsp;GHz'],
            'Maximum Boost Speed': ['3.8&nbsp;GHz', '3.2&nbsp;GHz',
                                    '2.9&nbsp;GHz'],
            'Total Installed Memory': ['16&nbsp;GB', '8&nbsp;GB',
                                    '8&nbsp;GB'],
            'Memory Type': ['LPDDR3&nbsp;SDRAM', 'LPDDR3&nbsp;SDRAM',
                            'LPDDR3&nbsp;SDRAM'],
            'Memory Speed': ['2133&nbsp;MHz', '1866&nbsp;MHz',
                            '1600&nbsp;MHz'],
            'Onboard Memory': ['16&nbsp;GB', '8&nbsp;GB', '8&nbsp;GB'],
            'Available Memory Slots': ['\xe2\x80\x94', '\xe2\x80\x94',
                                    '\xe2\x80\x94'],
            'Graphics Type': ['Hybrid', 'Integrated', 'Integrated'],
            'GPU': ['AMD Radeon&nbsp;Pro 555 with 2&nbsp;GB&nbsp;GDDR5 VRAM,<br>Intel HD Graphics&nbsp;630'
                    , 'Intel HD Graphics&nbsp;615',
                    'Intel HD Graphics&nbsp;6000'],
            }},
        {'name': 'Display', 'properties': {
            'Graphics Type': ['IPS', 'IPS', 'Not specified'],
            'Size': ['15.4"', '12"', '13.3"'],
            'Aspect Ratio': ['16:10', '16:10', '16:10'],
            'Native Resolution': ['2880\xc3\x971800', '2304\xc3\x971440',
                                '1440\xc3\x97900'],
            'Touchscreen': ['\xe2\x80\x94', '\xe2\x80\x94', '\xe2\x80\x94'
                            ],
            'Finish': ['Glossy', 'Glossy', 'Glossy'],
            'Brightness': ['500&nbsp;cd/m<sup>2</sup>', 'Not specified',
                        'Not specified'],
            'Viewing Angle': ['Not specified', 'Not specified',
                            'Not specified'],
            'Refresh Rate': ['Not specified', 'Not specified',
                            'Not specified'],
            'Response Time': ['Not specified', 'Not specified',
                            'Not specified'],
            'Adaptive Sync Technology': ['Not specified', 'Not specified',
                    'Not specified'],
            'External Resolution': ['Not specified', 'Not specified',
                                    'Not specified'],
            }},
        {'name': 'Drives', 'properties': {
            'Available Slots': ['\xe2\x80\x94', '\xe2\x80\x94',
                                '\xe2\x80\x94'],
            'Total Capacity': ['256&nbsp;GB', '512&nbsp;GB', '128&nbsp;GB'
                            ],
            'Solid State Storage': ['1 \xc3\x97 256&nbsp;GB&nbsp;Integrated PCIe'
                                    ,
                                    '1 \xc3\x97 512&nbsp;GB&nbsp;Integrated PCIe'
                                    ,
                                    '1 \xc3\x97 128&nbsp;GB&nbsp;Integrated PCIe'
                                    ],
            'Optical Drive': ['\xe2\x80\x94', '\xe2\x80\x94', '\xe2\x80\x94'
                            ],
            }},
        {'name': 'Input/ Output Connectors', 'properties': {
            'Ports': ['4 \xc3\x97 Thunderbolt 3&nbsp;via USB Type-C',
                    '1 \xc3\x97 USB 3.1 Gen 1&nbsp;Type-C',
                    '2 \xc3\x97 USB 3.1 Gen 1&nbsp;Type-A,<br>1 \xc3\x97 Thunderbolt 2'
                    ],
            'Display': ['4 \xc3\x97 DisplayPort&nbsp;via Type-C',
                        '1 \xc3\x97 DisplayPort&nbsp;1.2&nbsp;via Optional Cable,<br>1 \xc3\x97 HDMI&nbsp;via Optional Cable,<br>1 \xc3\x97 VGA&nbsp;via Optional Cable'
                        ,
                        '1 \xc3\x97 Mini DisplayPort&nbsp;via Thunderbolt Port'
                        ],
            'Audio': ['1 \xc3\x97 1/8" (3.5&nbsp;mm) Headphone Output,<br>2 \xc3\x97 Integrated Speaker,<br>3 \xc3\x97 Integrated Microphone'
                    ,
                    '1 \xc3\x97 1/8" (3.5&nbsp;mm) Headphone Output,<br>2 \xc3\x97 Integrated Speaker,<br>2 \xc3\x97 Integrated Microphone'
                    ,
                    '1 \xc3\x97 1/8" (3.5&nbsp;mm) Headphone Output,<br>2 \xc3\x97 Integrated Speaker,<br>2 \xc3\x97 Integrated Microphone'
                    ],
            'Expansion Slots': ['\xe2\x80\x94', '\xe2\x80\x94',
                                '\xe2\x80\x94'],
            'Media Card Slots': ['\xe2\x80\x94', '\xe2\x80\x94',
                                'SD/SDHC/SDXC'],
            }},
        {'name': 'Communications', 'properties': {
            'Network': ['\xe2\x80\x94', '\xe2\x80\x94', '\xe2\x80\x94'],
            'Modem': ['\xe2\x80\x94', '\xe2\x80\x94', '\xe2\x80\x94'],
            'Wi-Fi': ['802.11ac; Dual-Band', '802.11ac; Dual-Band',
                    '802.11ac; Dual-Band'],
            'Bluetooth': ['Bluetooth 4.2', 'Bluetooth 4.2', 'Bluetooth 4.0'
                        ],
            'Mobile Broadband': ['\xe2\x80\x94', '\xe2\x80\x94',
                                '\xe2\x80\x94'],
            'GPS': ['Not specified', '\xe2\x80\x94', 'Not specified'],
            'NFC': ['Not specified', '\xe2\x80\x94', 'Not specified'],
            'Webcam': ['User-Facing: 720p Video', 'User-Facing: 480p Video'
                    , 'User-Facing: 720p Video'],
            }},
        {'name': 'Battery', 'properties': {
            'Battery Chemistry': ['Lithium-Ion Polymer',
                                'Lithium-Ion Polymer',
                                'Lithium-Ion Polymer'],
            'Watt Hours / Type': ['76&nbsp;Wh&nbsp;Non-Removable',
                                '41.4&nbsp;Wh&nbsp;Non-Removable',
                                '54&nbsp;Wh&nbsp;Non-Removable'],
            'Cells': ['Not specified', 'Not specified', 'Not specified'],
            'Output Voltage': ['Not specified', 'Not specified',
                            'Not specified'],
            'Maximum Runtime': ['10&nbsp;Hours', '10&nbsp;Hours',
                                '12&nbsp;Hours'],
            'Power Requirements': ['100-240&nbsp;VAC, 50-60&nbsp;Hz',
                                '100-240&nbsp;VAC, 50-60&nbsp;Hz',
                                '100-240&nbsp;VAC, 50-60&nbsp;Hz'],
            'Power Supply': ['1 \xc3\x97 87&nbsp;W', '1 \xc3\x97 29&nbsp;W'
                            , '1 \xc3\x97 45&nbsp;W'],
            }},
        {'name': 'General', 'properties': {
            'Operating System': ['macOS High Sierra', 'macOS High Sierra',
                                'macOS High Sierra'],
            'Security': ['Not specified', 'Not specified', 'Not specified'
                        ],
            'Keyboard': ['Keys: 64,<br>type: Standard Notebook Keyboard,<br>Features: Backlight'
                        ,
                        'Keys: 78,<br>type: Standard Notebook Keyboard,<br>Features: Backlight'
                        ,
                        'Keys: 78,<br>type: Standard Notebook Keyboard,<br>Features: Backlight'
                        ],
            'Pointing Device': ['Force Touch Trackpad',
                                'Force Touch Trackpad', 'TouchPad'],
            'Dimensions (W \xc3\x97 H \xc3\x97 D)': ['13.8 \xc3\x97 0.6 \xc3\x97 9.5"&nbsp;/&nbsp;35.1 \xc3\x97 1.5 \xc3\x97 24.1&nbsp;cm'
                    ,
                    '11.0 \xc3\x97 0.5 \xc3\x97 7.7"&nbsp;/&nbsp;27.9 \xc3\x97 1.3 \xc3\x97 19.6&nbsp;cm'
                    ,
                    '12.8 \xc3\x97 0.7 \xc3\x97 8.9"&nbsp;/&nbsp;32.5 \xc3\x97 1.8 \xc3\x97 22.6&nbsp;cm'
                    ],
            'Weight': ['4.02&nbsp;lb&nbsp;/&nbsp;1.82&nbsp;kg',
                    '2.03&nbsp;lb&nbsp;/&nbsp;.92&nbsp;kg',
                    '2.96&nbsp;lb&nbsp;/&nbsp;1.34&nbsp;kg'],
            'Warranty Length': ['Limited 1-Year Warranty',
                                'Limited 1-Year Warranty',
                                'Limited 1-Year Warranty'],
            }},
        ]

    articles = [{
        'title': 'Everything You Need to Know About the MacBook Pro',
        'description': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales eget ipsum id aliquam. Nam consectetur interdum nibh eget sodales. Cras volutpat efficitur ornare.</p>'
            ,
        'preview': 'static/images/articles/macbook-photo.jpg',
        'date': 'May 21, 2018',
        'href': 'article.html',
        }, {
        'title': 'Apple introduces macOS Mojave',
        'description': '<p>Praesent consequat justo eu massa malesuada posuere. Donec ultricies tincidunt nisl, sed euismod nulla venenatis maximus. Maecenas sit amet semper tellus. Pellentesque imperdiet finibus sapien, a consectetur eros auctor a.</p>'
            ,
        'preview': 'static/images/articles/macos.jpg',
        'date': 'May 21, 2018',
        'href': 'article.html',
        }]

    news = [{
        'title': 'Highlights from WWDC',
        'description': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales eget ipsum id aliquam. Nam consectetur interdum nibh eget sodales. Cras volutpat efficitur ornare.</p>'
            ,
        'date': 'June 4, 2018',
        'href': 'article.html',
        }, {
        'title': 'Apple introduces macOS Mojave',
        'description': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales eget ipsum id aliquam. Nam consectetur interdum nibh eget sodales. Cras volutpat efficitur ornare.</p>'
            ,
        'date': 'June 4, 2018',
        'href': 'article.html',
        }, {
        'title': 'iOS 11.4 brings stereo pairs and multi-room audio with AirPlay 2'
            ,
        'description': '<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin sodales eget ipsum id aliquam. Nam consectetur interdum nibh eget sodales. Cras volutpat efficitur ornare.</p>'
            ,
        'date': 'May 29, 2018',
        'href': 'article.html',
        }]

    profile = {
        'firstname': 'Thomas',
        'lastname': 'Bruns',
        'image': 'static/images/avatar.jpg',
        'registrationdate': 'June 6, 2018',
        'phone': '8 (800) 555-35-35',
        'dateOFBirth': '1990-01-01',
        'email': 'example@example.com',
        }

    profileNav = [{
        'id': 1,
        'title': 'Orders',
        'amount': 2,
        'href': 'account.html',
        }, {
        'id': 2,
        'title': 'Favorites',
        'amount': 3,
        'href': 'favorites.html',
        }, {'id': 3, 'title': 'Personal Info', 'href': 'personal.html'}]

    orders = [{
        'id': '36637649',
        'date': 'June 17, 2018',
        'items_': 7,
        'shipping': 'Pick up from store',
        'payment': 'Online by card',
        'total': '$4896.00',
        'status': 'Processing',
        }, {
        'id': '36637648',
        'date': 'June 16, 2018',
        'items_': 2,
        'shipping': 'Pick up from store',
        'payment': 'Online by card',
        'total': '$599.00',
        'status': 'Canceled',
        }]

    informationalNav = [
        {'id': 1, 'title': 'About', 'href': 'about.html'},
        {'id': 2, 'title': 'Contacts', 'href': 'contacts.html'},
        {'id': 3, 'title': 'Blog', 'href': 'blog.html'},
        {'id': 4, 'title': 'News', 'href': 'news.html'},
        {'id': 5, 'title': 'FAQ', 'href': 'faq.html'},
        {'id': 6, 'title': 'Delivery', 'href': 'delivery.html'},
        ]

    promo = [{'background': '#0b0a12',
            'image': 'static/images/promo/macbook-new.jpg', 'title': 'New Macbook'
            }, {'background': '#ce071e', 'image': 'static/images/promo/iphone.jpg'
            , 'title': 'iPhone'}, {'background': '#1f2024',
            'image': 'static/images/promo/ipad.jpg', 'title': 'iPad'}]

    categories = [
        {
            'title': 'Laptops',
            'href': 'subcategory.html',
            'comment': 'from $149',
            'image': 'static/images/catalog/laptops.png',
            },
        {
            'title': 'Smartphones',
            'href': 'subcategory.html',
            'comment': 'from $99',
            'image': 'static/images/catalog/smartphones.png',
            },
        {
            'title': 'Tablets',
            'href': 'subcategory.html',
            'comment': 'from $129',
            'image': 'static/images/catalog/tablets.png',
            },
        {
            'title': 'Smart Watches',
            'href': 'subcategory.html',
            'comment': 'from $49',
            'image': 'static/images/catalog/watches.png',
            },
        {
            'title': 'Gaming Consoles',
            'href': 'subcategory.html',
            'comment': 'from $399',
            'image': 'static/images/catalog/consoles.png',
            },
        {
            'title': 'Cameras',
            'href': 'subcategory.html',
            'comment': 'from $129',
            'image': 'static/images/catalog/cameras.png',
            },
        ]

    advantages = [{'title': 'Mauris placerat',
                'description': 'Donec mollis nibh dolor, sit amet auctor'
                , 'icon': 'star'}, {'title': 'Lorem ipsum',
                'description': 'Sit amet, consectetur adipiscing elit',
                'icon': 'receiver'}, {'title': 'Proin pharetra',
                'description': 'Nec quam a fermentum ut viverra',
                'icon': 'location'}, {'title': 'Praesent ultrices',
                'description': 'Praesent ultrices, orci nec finibus',
                'icon': 'comments'}, {'title': 'Duis condimentum',
                'description': 'Pellentesque eget varius arcu',
                'icon': 'happy'}]

