import customtkinter as ctk


class Theme:
    APP_NAME = "ShopEase"

    WINDOW_WIDTH = 460
    WINDOW_HEIGHT = 560

    PRIMARY_COLOR = "#1f6aa5"
    HOVER_COLOR = "#144870"

    BG_COLOR = "#111827"
    CARD_COLOR = "#1f2937"
    TEXT_COLOR = "#ffffff"
    SUBTEXT_COLOR = "#9ca3af"

    FONT_TITLE = ("Arial", 32, "bold")
    FONT_SUBTITLE = ("Arial", 16)
    FONT_NORMAL = ("Arial", 14)
    FONT_BUTTON = ("Arial", 15, "bold")

    @staticmethod
    def apply_theme():
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")