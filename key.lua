--//====================================================--
--// Eymnfox Premium Brookhaven Client Utility
--// Sadece CLIENT-SIDE çalışır.
--// Başka oyunculara hiçbir etkisi yoktur.
--//====================================================--

--// Eymnfox özel yorum satırı :)
--// "Detaylar kaliteyi oluşturur."

local Players = game:GetService("Players")
local TweenService = game:GetService("TweenService")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local Lighting = game:GetService("Lighting")
local Stats = game:GetService("Stats")
local SoundService = game:GetService("SoundService")

local LocalPlayer = Players.LocalPlayer
local PlayerGui = LocalPlayer:WaitForChild("PlayerGui")

local Character = LocalPlayer.Character or LocalPlayer.CharacterAdded:Wait()
local Humanoid = Character:WaitForChild("Humanoid")

--//====================================================--
--// BLUR
--//====================================================--

local blur = Instance.new("BlurEffect")
blur.Name = "EymnfoxBlur"
blur.Size = 14
blur.Parent = Lighting

--//====================================================--
--// GUI
--//====================================================--

local ScreenGui = Instance.new("ScreenGui")
ScreenGui.Name = "EymnfoxUI"
ScreenGui.ResetOnSpawn = false
ScreenGui.ZIndexBehavior = Enum.ZIndexBehavior.Sibling
ScreenGui.Parent = PlayerGui

--====================================================--
-- INFO PANEL
--====================================================--

local InfoPanel = Instance.new("Frame")
InfoPanel.Size = UDim2.new(0, 180, 0, 82)
InfoPanel.Position = UDim2.new(0, 15, 0, 15)
InfoPanel.BackgroundColor3 = Color3.fromRGB(15, 25, 55)
InfoPanel.BackgroundTransparency = 0.22
InfoPanel.Parent = ScreenGui

local InfoCorner = Instance.new("UICorner")
InfoCorner.CornerRadius = UDim.new(0, 14)
InfoCorner.Parent = InfoPanel

local InfoStroke = Instance.new("UIStroke")
InfoStroke.Color = Color3.fromRGB(0, 170, 255)
InfoStroke.Thickness = 1.6
InfoStroke.Parent = InfoPanel

local InfoGradient = Instance.new("UIGradient")
InfoGradient.Rotation = 45
InfoGradient.Color = ColorSequence.new{
	ColorSequenceKeypoint.new(0, Color3.fromRGB(0, 120, 255)),
	ColorSequenceKeypoint.new(1, Color3.fromRGB(0, 40, 100))
}
InfoGradient.Parent = InfoPanel

local InfoTitle = Instance.new("TextLabel")
InfoTitle.BackgroundTransparency = 1
InfoTitle.Size = UDim2.new(1,0,0,28)
InfoTitle.Text = "Eymnfox"
InfoTitle.Font = Enum.Font.GothamBlack
InfoTitle.TextSize = 22
InfoTitle.TextColor3 = Color3.fromRGB(120,220,255)
InfoTitle.Parent = InfoPanel

local FPSLabel = Instance.new("TextLabel")
FPSLabel.BackgroundTransparency = 1
FPSLabel.Position = UDim2.new(0,10,0,32)
FPSLabel.Size = UDim2.new(1,-20,0,18)
FPSLabel.Font = Enum.Font.Gotham
FPSLabel.TextSize = 14
FPSLabel.TextXAlignment = Enum.TextXAlignment.Left
FPSLabel.Text = "FPS: ..."
FPSLabel.TextColor3 = Color3.new(1,1,1)
FPSLabel.Parent = InfoPanel

local PingLabel = Instance.new("TextLabel")
PingLabel.BackgroundTransparency = 1
PingLabel.Position = UDim2.new(0,10,0,50)
PingLabel.Size = UDim2.new(1,-20,0,18)
PingLabel.Font = Enum.Font.Gotham
PingLabel.TextSize = 14
PingLabel.TextXAlignment = Enum.TextXAlignment.Left
PingLabel.Text = "Ping: ..."
PingLabel.TextColor3 = Color3.new(1,1,1)
PingLabel.Parent = InfoPanel

local SessionLabel = Instance.new("TextLabel")
SessionLabel.BackgroundTransparency = 1
SessionLabel.Position = UDim2.new(0,10,0,66)
SessionLabel.Size = UDim2.new(1,-20,0,14)
SessionLabel.Font = Enum.Font.Gotham
SessionLabel.TextSize = 12
SessionLabel.TextXAlignment = Enum.TextXAlignment.Left
SessionLabel.Text = "Session: 0s"
SessionLabel.TextColor3 = Color3.fromRGB(180,220,255)
SessionLabel.Parent = InfoPanel

--====================================================--
-- MAIN PANEL
--====================================================--

local MainFrame = Instance.new("Frame")
MainFrame.AnchorPoint = Vector2.new(0.5,0.5)
MainFrame.Position = UDim2.new(0.5,0,0.5,0)
MainFrame.Size = UDim2.new(0,0,0,0)
MainFrame.BackgroundColor3 = Color3.fromRGB(15,25,55)
MainFrame.BackgroundTransparency = 0.18
MainFrame.Parent = ScreenGui

MainFrame.Active = true
MainFrame.Draggable = true

local MainCorner = Instance.new("UICorner")
MainCorner.CornerRadius = UDim.new(0,18)
MainCorner.Parent = MainFrame

local MainStroke = Instance.new("UIStroke")
MainStroke.Color = Color3.fromRGB(0,170,255)
MainStroke.Thickness = 2
MainStroke.Parent = MainFrame

local MainGradient = Instance.new("UIGradient")
MainGradient.Rotation = 45
MainGradient.Color = ColorSequence.new{
	ColorSequenceKeypoint.new(0, Color3.fromRGB(0,120,255)),
	ColorSequenceKeypoint.new(1, Color3.fromRGB(0,45,110))
}
MainGradient.Parent = MainFrame

local Shine = Instance.new("Frame")
Shine.BackgroundTransparency = 0.96
Shine.BackgroundColor3 = Color3.new(1,1,1)
Shine.Size = UDim2.new(1,0,1,0)
Shine.Parent = MainFrame

local ShineCorner = Instance.new("UICorner")
ShineCorner.CornerRadius = UDim.new(0,18)
ShineCorner.Parent = Shine

--====================================================--
-- OPEN ANIMATION
--====================================================--

TweenService:Create(
	MainFrame,
	TweenInfo.new(0.45, Enum.EasingStyle.Quint),
	{
		Size = UDim2.new(0,340,0,260)
	}
):Play()

--====================================================--
-- TITLE
--====================================================--

local Title = Instance.new("TextLabel")
Title.BackgroundTransparency = 1
Title.Size = UDim2.new(1,0,0,45)
Title.Text = "Eymnfox"
Title.Font = Enum.Font.GothamBlack
Title.TextSize = 30
Title.TextColor3 = Color3.fromRGB(120,220,255)
Title.Parent = MainFrame

--====================================================--
-- SOUNDS
--====================================================--

local ClickSound = Instance.new("Sound")
ClickSound.SoundId = "rbxassetid://9118823108"
ClickSound.Volume = 0.2
ClickSound.Parent = SoundService

--====================================================--
-- NOTIFICATION SYSTEM
--====================================================--

local function Notify(text)
	local NotifyFrame = Instance.new("Frame")
	NotifyFrame.Size = UDim2.new(0,220,0,42)
	NotifyFrame.Position = UDim2.new(1,-240,1,-70)
	NotifyFrame.BackgroundColor3 = Color3.fromRGB(0,120,255)
	NotifyFrame.BackgroundTransparency = 0.12
	NotifyFrame.Parent = ScreenGui

	local NC = Instance.new("UICorner")
	NC.CornerRadius = UDim.new(0,12)
	NC.Parent = NotifyFrame

	local Label = Instance.new("TextLabel")
	Label.BackgroundTransparency = 1
	Label.Size = UDim2.new(1,0,1,0)
	Label.Text = text
	Label.Font = Enum.Font.GothamBold
	Label.TextSize = 15
	Label.TextColor3 = Color3.new(1,1,1)
	Label.Parent = NotifyFrame

	TweenService:Create(
		NotifyFrame,
		TweenInfo.new(0.3),
		{
			Position = UDim2.new(1,-240,1,-100)
		}
	):Play()

	task.delay(3,function()
		TweenService:Create(
			NotifyFrame,
			TweenInfo.new(0.3),
			{
				BackgroundTransparency = 1
			}
		):Play()

		task.wait(0.3)
		NotifyFrame:Destroy()
	end)
end

Notify("Eymnfox Loaded")

--====================================================--
-- WALKSPEED
--====================================================--

local WSLabel = Instance.new("TextLabel")
WSLabel.BackgroundTransparency = 1
WSLabel.Position = UDim2.new(0,20,0,70)
WSLabel.Size = UDim2.new(0,130,0,30)
WSLabel.Text = "WalkSpeed"
WSLabel.Font = Enum.Font.Gotham
WSLabel.TextSize = 18
WSLabel.TextColor3 = Color3.new(1,1,1)
WSLabel.Parent = MainFrame

local WSBox = Instance.new("TextBox")
WSBox.Position = UDim2.new(0,170,0,70)
WSBox.Size = UDim2.new(0,140,0,30)
WSBox.BackgroundColor3 = Color3.fromRGB(20,45,100)
WSBox.TextColor3 = Color3.new(1,1,1)
WSBox.PlaceholderText = "16"
WSBox.Text = ""
WSBox.Font = Enum.Font.Gotham
WSBox.TextSize = 16
WSBox.Parent = MainFrame

local WSCorner = Instance.new("UICorner")
WSCorner.Parent = WSBox

--====================================================--
-- JUMPPOWER
--====================================================--

local JPLabel = Instance.new("TextLabel")
JPLabel.BackgroundTransparency = 1
JPLabel.Position = UDim2.new(0,20,0,120)
JPLabel.Size = UDim2.new(0,130,0,30)
JPLabel.Text = "JumpPower"
JPLabel.Font = Enum.Font.Gotham
JPLabel.TextSize = 18
JPLabel.TextColor3 = Color3.new(1,1,1)
JPLabel.Parent = MainFrame

local JPBox = Instance.new("TextBox")
JPBox.Position = UDim2.new(0,170,0,120)
JPBox.Size = UDim2.new(0,140,0,30)
JPBox.BackgroundColor3 = Color3.fromRGB(20,45,100)
JPBox.TextColor3 = Color3.new(1,1,1)
JPBox.PlaceholderText = "50"
JPBox.Text = ""
JPBox.Font = Enum.Font.Gotham
JPBox.TextSize = 16
JPBox.Parent = MainFrame

local JPCorner = Instance.new("UICorner")
JPCorner.Parent = JPBox

--====================================================--
-- GLOW BUTTON
--====================================================--

local GlowButton = Instance.new("TextButton")
GlowButton.Position = UDim2.new(0.5,-100,0,185)
GlowButton.Size = UDim2.new(0,200,0,42)
GlowButton.BackgroundColor3 = Color3.fromRGB(0,120,255)
GlowButton.Text = "Glow : OFF"
GlowButton.Font = Enum.Font.GothamBold
GlowButton.TextSize = 18
GlowButton.TextColor3 = Color3.new(1,1,1)
GlowButton.Parent = MainFrame

local GlowCorner = Instance.new("UICorner")
GlowCorner.Parent = GlowButton

--====================================================--
-- HOVER EFFECT
--====================================================--

GlowButton.MouseEnter:Connect(function()
	TweenService:Create(
		GlowButton,
		TweenInfo.new(0.15),
		{
			BackgroundTransparency = 0.12
		}
	):Play()
end)

GlowButton.MouseLeave:Connect(function()
	TweenService:Create(
		GlowButton,
		TweenInfo.new(0.15),
		{
			BackgroundTransparency = 0
		}
	):Play()
end)

--====================================================--
-- HIGHLIGHT
--====================================================--

local Highlight = Instance.new("Highlight")
Highlight.FillColor = Color3.fromRGB(0,170,255)
Highlight.OutlineColor = Color3.fromRGB(100,220,255)
Highlight.FillTransparency = 0.35
Highlight.OutlineTransparency = 0
Highlight.Enabled = false
Highlight.Parent = Character

local GlowEnabled = false

GlowButton.MouseButton1Click:Connect(function()

	ClickSound:Play()

	GlowEnabled = not GlowEnabled
	Highlight.Enabled = GlowEnabled

	if GlowEnabled then

		GlowButton.Text = "Glow : ON"

		TweenService:Create(
			GlowButton,
			TweenInfo.new(0.25),
			{
				BackgroundColor3 = Color3.fromRGB(0,180,255)
			}
		):Play()

		Notify("Glow Enabled")

	else

		GlowButton.Text = "Glow : OFF"

		TweenService:Create(
			GlowButton,
			TweenInfo.new(0.25),
			{
				BackgroundColor3 = Color3.fromRGB(0,120,255)
			}
		):Play()

		Notify("Glow Disabled")
	end
end)

--====================================================--
-- BREATHING GLOW
--====================================================--

task.spawn(function()
	while true do

		if Highlight.Enabled then

			TweenService:Create(
				Highlight,
				TweenInfo.new(1),
				{
					FillTransparency = 0.5
				}
			):Play()

			task.wait(1)

			TweenService:Create(
				Highlight,
				TweenInfo.new(1),
				{
					FillTransparency = 0.25
				}
			):Play()
		end

		task.wait(1)
	end
end)

--====================================================--
-- UI BORDER PULSE
--====================================================--

task.spawn(function()
	while true do

		TweenService:Create(
			MainStroke,
			TweenInfo.new(1),
			{
				Transparency = 0.3
			}
		):Play()

		task.wait(1)

		TweenService:Create(
			MainStroke,
			TweenInfo.new(1),
			{
				Transparency = 0
			}
		):Play()

		task.wait(1)
	end
end)

--====================================================--
-- WALKSPEED APPLY
--====================================================--

WSBox.FocusLost:Connect(function()

	local Value = tonumber(WSBox.Text)

	if Value and Value >= 0 and Value <= 200 then
		Humanoid.WalkSpeed = Value
		Notify("WalkSpeed set to "..Value)
	end
end)

--====================================================--
-- JUMPPOWER APPLY
--====================================================--

JPBox.FocusLost:Connect(function()

	local Value = tonumber(JPBox.Text)

	if Value and Value >= 0 and Value <= 300 then
		Humanoid.JumpPower = Value
		Notify("JumpPower set to "..Value)
	end
end)

--====================================================--
-- PARALLAX EFFECT
--====================================================--

UserInputService.InputChanged:Connect(function(input)

	if input.UserInputType == Enum.UserInputType.MouseMovement then

		local viewport = workspace.CurrentCamera.ViewportSize

		local x = (input.Position.X / viewport.X - 0.5) * 6
		local y = (input.Position.Y / viewport.Y - 0.5) * 6

		MainFrame.Position = UDim2.new(
			0.5,
			x,
			0.5,
			y
		)
	end
end)

--====================================================--
-- TOGGLE UI
--====================================================--

UserInputService.InputBegan:Connect(function(input,gp)

	if gp then return end

	if input.KeyCode == Enum.KeyCode.RightShift then

		ClickSound:Play()

		MainFrame.Visible = not MainFrame.Visible
		InfoPanel.Visible = not InfoPanel.Visible

		if MainFrame.Visible then
			Notify("UI Opened")
		else
			Notify("UI Hidden")
		end
	end
end)

--====================================================--
-- FPS + PING
--====================================================--

local Last = tick()
local StartSession = tick()

RunService.RenderStepped:Connect(function()

	local Current = tick()

	local FPS = math.floor(1 / (Current - Last))
	Last = Current

	FPSLabel.Text = "FPS : "..FPS

	if FPS >= 60 then
		FPSLabel.TextColor3 = Color3.fromRGB(0,255,120)
	elseif FPS >= 30 then
		FPSLabel.TextColor3 = Color3.fromRGB(255,170,0)
	else
		FPSLabel.TextColor3 = Color3.fromRGB(255,80,80)
	end

	local Ping = math.floor(
		Stats.Network.ServerStatsItem["Data Ping"]:GetValue()
	)

	if Ping > 150 then
		PingLabel.Text = "Ping : "..Ping.." ms ⚠"
		PingLabel.TextColor3 = Color3.fromRGB(255,120,120)
	else
		PingLabel.Text = "Ping : "..Ping.." ms"
		PingLabel.TextColor3 = Color3.new(1,1,1)
	end

	local Session = math.floor(tick() - StartSession)
	SessionLabel.Text = "Session : "..Session.."s"
end)

--====================================================--
-- CHARACTER RESPAWN
--====================================================--

LocalPlayer.CharacterAdded:Connect(function(char)

	Character = char
	Humanoid = char:WaitForChild("Humanoid")

	Highlight.Parent = Character

	if GlowEnabled then
		Highlight.Enabled = true
	end

	Notify("Character Reloaded")
end)
