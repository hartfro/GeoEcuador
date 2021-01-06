extends Node2D
class_name Region

export(NodePath) var InfoLabel
onready var children = get_children()

func _ready():
	InfoLabel = get_node(InfoLabel)
	# Set default script variables.
	if not InfoLabel or not InfoLabel is Label:
		InfoLabel = Label.new()
		add_child(InfoLabel)
		
	# Override children InfoLabel
	for child in children:
		if child is Provincia and child.has_own_info_label:
			child.InfoLabel = InfoLabel
			child.has_own_info_label = false 
