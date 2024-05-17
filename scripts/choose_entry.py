import cv2


# handling user input on image
def mouse_callback(event, x, y, flags, param):
    points, image = param
    if event == cv2.EVENT_LBUTTONDOWN:
        if len(points) < 2:
            points.append((x, y))
            print("Wybrano punkt:", (x, y))
            cv2.circle(image, (x, y), 5, (0, 0, 255), -1)
            cv2.imshow("Wybierz punkty", image)
        else:
            print("Maksymalna liczba punktów została osiągnięta")


def read_image(video_name, frame_number):
    cap = cv2.VideoCapture(video_name)

    if not cap.isOpened():
        print("Błąd: Nie udało się wczytać filmu.")
        exit()

    cap.set(cv2.CAP_PROP_POS_FRAMES, frame_number)
    ret, frame = cap.read()

    if not ret:
        print("Błąd: Nie udało się odczytać pierwszej klatki.")
        exit()

    cap.release()
    return frame


def draw_square(points, image):
    if len(points) == 2:
        cv2.rectangle(image, points[0], points[1], (0, 0, 255), 2)
        cv2.imshow("Wybierz punkty", image)


# manual choosing of a bee entry/leaving point
def choose_entry_box(video_path, frame_number):
    image = read_image(video_path, frame_number)
    # cv2.imwrite('saved_image.jpg', image)
    points = []

    print(f"image shape: {image.shape[0]} {image.shape[1]}")
    cv2.namedWindow("Wybierz punkty")
    cv2.setMouseCallback("Wybierz punkty", mouse_callback, (points, image))


    while True:
        cv2.imshow("Wybierz punkty", image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        if len(points) == 2:
            draw_square(points, image)
            break

    # while cv2.waitKey(1) & 0xFF != ord('q'):
    #     pass
    cv2.destroyAllWindows()
    
    cv2.waitKey(1) # okno sie nie zamyka wiec daje to i dziala lol

    return [points[0][0], points[0][1], points[1][0], points[1][1]]
