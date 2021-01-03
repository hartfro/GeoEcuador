extends Area2D

export(String) var province_name
export(PackedScene) var Polygon
export(NodePath) var InfoLabel

var mouse_over = false

func _ready():
	# Set default Script Variables.
	if Polygon:
		remove_child($CollisionShape2D)
		add_child(Polygon.instance())
		
	if not province_name:
		province_name = name
		
	if not InfoLabel or not InfoLabel is Label:
		InfoLabel = Label.new()
		add_child(InfoLabel)
		InfoLabel.text = province_name
		
	InfoLabel.hide()


func _on_Provincia_input_event(viewport, event, shape_idx):
	if event is InputEventMouseButton and event.button_index == BUTTON_LEFT \
			&& event.pressed:
		InfoLabel.show()

func _input(event):
	# Handle press outside of Province.
	if (event is InputEventMouseButton) and event.pressed and !mouse_over:
		InfoLabel.hide()


func _on_Provincia_mouse_entered():
	mouse_over = true


func _on_Provincia_mouse_exited():
	mouse_over = false
