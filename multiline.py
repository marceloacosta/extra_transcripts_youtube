def main():
    urls_env = "https://www.youtube.com/watch?v=iBa9EoEbb38,https://www.youtube.com/watch?v=yuy9yQlFZAU,https://www.youtube.com/watch?v=Wasnm1xBmgI"
    urls = urls_env.split(',')
    for url in urls:
        print("Processing URL:", url)

if __name__ == "__main__":
    main()
