import torch
from torch import nn

# Transformer մոդելի դասի սահմանում
class TransformerModel(nn.Module):
    # Կոնստրուկտոր՝ մոդելի հիմնական բաղադրիչները ստեղծելու համար
    def __init__(self, input_dim, model_dim, num_heads, num_layers, ff_dim, vocab_size, max_len):
        super(TransformerModel, self).__init__()

        # Նշանների ներդրման շերտ՝ մուտքային նշանները մոդելի չափսով վեկտորների վերածելու համար
        self.token_embedding = nn.Embedding(vocab_size, model_dim)
        
        # Դիրքային կոդավորումների ստեղծում՝ հաջորդականության մեջ նշանների դիրքը փոխանցելու համար
        self.positional_encoding = nn.Parameter(
            self._generate_positional_encoding(max_len, model_dim), 
            requires_grad=False
        )

        # Կոդավորիչի շերտ՝ ինքնաուշադրության և feed-forward մեխանիզմներով
        self.encoder_layer = nn.TransformerEncoderLayer(d_model=model_dim, nhead=num_heads, dim_feedforward=ff_dim)
        self.encoder = nn.TransformerEncoder(self.encoder_layer, num_layers=num_layers)

        # Դեկոդավորիչի շերտ՝ նպատակային հաջորդականությունը ստեղծելու համար
        self.decoder_layer = nn.TransformerDecoderLayer(d_model=model_dim, nhead=num_heads, dim_feedforward=ff_dim)
        self.decoder = nn.TransformerDecoder(self.decoder_layer, num_layers=num_layers)

        # Վերջնական լիովին կապված շերտ՝ բառարանի վրա կանխատեսումներ անելու համար
        self.fc_out = nn.Linear(model_dim, vocab_size)

    # Ֆունկցիա՝ դիրքային կոդավորումներ ստեղծելու համար
    def _generate_positional_encoding(self, max_len, model_dim):
        # Ստեղծում է դիրքային կոդավորումներ՝ օգտագործելով սինուսոիդային ֆունկցիաներ
        pos = torch.arange(0, max_len).unsqueeze(1)  # Հաջորդականության դիրքերը
        i = torch.arange(0, model_dim, 2)  # Զույգ ինդեքսները
        angle_rates = 1 / torch.pow(10000, (2 * i / model_dim))  # Կոդավորման հաճախությունները
        
        positional_encoding = torch.zeros(max_len, model_dim)
        positional_encoding[:, 0::2] = torch.sin(pos * angle_rates)  # Զույգ ինդեքսների համար
        positional_encoding[:, 1::2] = torch.cos(pos * angle_rates)  # Կենտ ինդեքսների համար
        
        return positional_encoding.unsqueeze(0)  # Վերադարձնում է դիրքային կոդավորումները

    # Առաջանցիկ անցում՝ մուտքային տվյալները մշակելու և ելք տրամադրելու համար
    def forward(self, src, tgt, src_mask=None, tgt_mask=None):
        # Մուտքային նշաններին ավելացնում է ներդրումներն ու դիրքային կոդավորումները
        src = self.token_embedding(src) + self.positional_encoding[:, :src.size(1), :]
        tgt = self.token_embedding(tgt) + self.positional_encoding[:, :tgt.size(1), :]

        # Աղբյուրային հաջորդականության կոդավորումը
        memory = self.encoder(src, src_key_padding_mask=src_mask)

        # Նպատակային հաջորդականության դեկոդավորումը՝ օգտագործելով կոդավորիչի ելքը որպես հիշողություն
        output = self.decoder(tgt, memory, tgt_mask=tgt_mask, memory_key_padding_mask=src_mask)

        # Վերադարձնում է ելքը, որը ներկայացնում է բառարանի հավանականությունների բաշխումը
        return self.fc_out(output)

# Հիպերպարամետրերի սահմանում
vocab_size = 10000  # Բառարանի չափը
model_dim = 512  # Մոդելի չափսը
num_heads = 8  # Ուշադրության գլխերի քանակը
num_layers = 6  # Կոդավորիչի և դեկոդավորիչի շերտերի քանակը
ff_dim = 2048  # Feed-forward շերտի չափսը
max_len = 100  # Հաջորդականության առավելագույն երկարությունը

# Մոդելի ստեղծում՝ նշված հիպերպարամետրերով
model = TransformerModel(
    input_dim=model_dim, 
    model_dim=model_dim, 
    num_heads=num_heads, 
    num_layers=num_layers, 
    ff_dim=ff_dim, 
    vocab_size=vocab_size, 
    max_len=max_len
)

# Օրինակ տվյալներ՝ աղբյուրային և նպատակային հաջորդականությունների համար
src = torch.randint(0, vocab_size, (2, 10))  # Պատահական նշաններ որպես մուտք
tgt = torch.randint(0, vocab_size, (2, 10))  # Պատահական նշաններ որպես նպատակ

# Մոդելի վրա առաջանցիկ անցում
output = model(src, tgt)
print("Output shape:", output.shape)  # Ելքի չափս՝ (batch_size, sequence_length, vocab_size)

# Կորստի հաշվարկ՝ օգտագործելով խաչմերուկային էնտրոպիա
criterion = nn.CrossEntropyLoss()  # Կորստի ֆունկցիա
target_labels = torch.randint(0, vocab_size, (2, 10))  # Պատահական պիտակներ որպես նպատակ

# Ելքի և պիտակների վերաձևում՝ կորստի հաշվարկի համար
output_reshaped = output.view(-1, vocab_size)  # Ելքի չափս՝ (batch_size * sequence_length, vocab_size)
target_labels_reshaped = target_labels.view(-1)  # Նպատակ պիտակների չափս՝ (batch_size * sequence_length)

# Կորստի հաշվարկ
loss = criterion(output_reshaped, target_labels_reshaped)
print("Loss:", loss.item())  # Տպում է կորստի արժեքը






