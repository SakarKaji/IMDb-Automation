# url = "https://www.imdb.com/"
excel_file = "files\Movies.xlsx"
search_path = '//*[@id="suggestion-search"]'
search_icon = '//*[@id="suggestion-search-button"]'
movie_path = "//a[@class='more-results-ft-chip ipc-chip ipc-chip--on-base']"
tv_movie_path = "//a[@class='more-results-tv-chip ipc-chip ipc-chip--on-base']"
exact_results = "//section[@data-testid='find-results-section-title']//span[@class='ipc-btn__text'][normalize-space()='Exact matches']"
movie_list = '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li'


# # url = "https://www.imdb.com/"
# excel_file = "files\Movies.xlsx"
# search_path = '//*[@id="suggestion-search"]'
# movie_path = "//a[@class='more-results-ft-chip ipc-chip ipc-chip--on-base']"
# tv_movie_path = "//a[@class='more-results-tv-chip ipc-chip ipc-chip--on-base']"
# storyline_visible = "//span[normalize-space()='Storyline']"
# plot_summary_load = "//a[normalize-space()='Plot summary']"

# # rating_xpath = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[2]/div[2]/div/div[1]/a/span/div/div[2]/div[1]/span[1]'
# rating_xpath = "//div[@data-testid='hero-rating-bar__aggregate-rating__score']//span[@class='sc-bde20123-1 cMEQkK']"
# # rating_xpath = '//*[@id="__next"]/main/div/section[1]/section/div[3]/section/section/div[3]/div[2]/div[2]/div[1]/div/div[1]/a/span/div/div[2]/div[1]'
# popularity_xpath = '//div[@data-testid="hero-rating-bar__popularity__score"]'
# storyline_xpath = "//div[@data-testid='storyline-plot-summary']"
# genre_xpath = "//li[@data-testid='storyline-genres']//ul[@role='presentation']//li"
# review_xpath = "//a[normalize-space()='User reviews']"
# dropdown_xpath = "//select[@name='sort']"
# title_elements = "//a[@class='title']"
# rating_review_elements = '//span[@class="rating-other-user-rating"]'
# expander_xpath = '//*[@class="expander-icon-wrapper spoiler-warning__control"]'
# review_container_xpath = "//div[@class='text show-more__control']"   
# exact_results = "//section[@data-testid='find-results-section-title']//span[@class='ipc-btn__text'][normalize-space()='Exact matches']"
# # movie_list = '//*[@id="__next"]/main/div[2]/div[3]/section/div/div[1]/section[2]/div[2]/ul/li'
# movie_list = "//*[@class='ipc-metadata-list-summary-item ipc-metadata-list-summary-item--click find-result-item find-title-result']"