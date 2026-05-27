package com.hp.print.horizontalconnector.ui.main;
 
import android.os.Bundle;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.Fragment;
import android.support.v7.widget.LinearLayoutManager;
import android.support.v7.widget.RecyclerView;
import android.text.TextUtils;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.Button;
import android.widget.EditText;
import android.widget.ProgressBar;
import android.widget.TextView;
 
import com.hp.print.horizontalconnector.R;
 
import java.util.ArrayList;
import java.util.List;
 
public class CopilotChatFragment extends Fragment {
 
    private RecyclerView recyclerView;
    private EditText inputEditText;
    private Button sendButton;
    private ProgressBar progressBar;
    private ChatAdapter adapter;
    private List<ChatMessage> chatMessages = new ArrayList<>();
 
    @Nullable
    @Override
    public View onCreateView(@NonNull LayoutInflater inflater, @Nullable ViewGroup container,
                             @Nullable Bundle savedInstanceState) {
        View view = inflater.inflate(R.layout.fragment_copilot_chat, container, false);
        recyclerView = view.findViewById(R.id.copilot_chat_recycler_view);
        inputEditText = view.findViewById(R.id.copilot_chat_input);
        sendButton = view.findViewById(R.id.copilot_chat_send);
        progressBar = view.findViewById(R.id.copilot_chat_progress);
 
        adapter = new ChatAdapter(chatMessages);
        recyclerView.setLayoutManager(new LinearLayoutManager(getContext()));
        recyclerView.setAdapter(adapter);
 
        sendButton.setOnClickListener(v -> sendMessage());
 
        return view;
    }
 
    private void sendMessage() {
        String userInput = inputEditText.getText().toString().trim();
        if (TextUtils.isEmpty(userInput)) return;
 
        addMessage(new ChatMessage(userInput, true));
        inputEditText.setText(\"\");
        progressBar.setVisibility(View.VISIBLE);
 
        // Simulate API call to Copilot Chat API (Replace with actual integration)
        // For demo, echo the input after delay
        recyclerView.postDelayed(() -> {
            addMessage(new ChatMessage(\"Copilot: \" + userInput, false));
            progressBar.setVisibility(View.GONE);
        }, 1000);
    }
 
    private void addMessage(ChatMessage message) {
        chatMessages.add(message);
        adapter.notifyItemInserted(chatMessages.size() - 1);
        recyclerView.smoothScrollToPosition(chatMessages.size() - 1);
    }
 
    // Simple chat message model
    private static class ChatMessage {
        final String text;
        final boolean isUser;
 
        ChatMessage(String text, boolean isUser) {
            this.text = text;
            this.isUser = isUser;
        }
    }
 
    // Simple adapter for chat messages
    private static class ChatAdapter extends RecyclerView.Adapter<ChatAdapter.ChatViewHolder> {
        private final List<ChatMessage> messages;
 
        ChatAdapter(List<ChatMessage> messages) {
            this.messages = messages;
        }
 
        @NonNull
        @Override
        public ChatViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
            View v = LayoutInflater.from(parent.getContext())
                    .inflate(R.layout.item_copilot_chat_message, parent, false);
            return new ChatViewHolder(v);
        }
 
        @Override
        public void onBindViewHolder(@NonNull ChatViewHolder holder, int position) {
            ChatMessage msg = messages.get(position);
            holder.messageText.setText(msg.text);
            holder.messageText.setGravity(msg.isUser ? View.TEXT_ALIGNMENT_TEXT_END : View.TEXT_ALIGNMENT_TEXT_START);
        }
 
        @Override
        public int getItemCount() {
            return messages.size();
        }
 
        static class ChatViewHolder extends RecyclerView.ViewHolder {
            TextView messageText;
 
            ChatViewHolder(View itemView) {
                super(itemView);
                messageText = itemView.findViewById(R.id.copilot_chat_message_text);
            }
        }
    }
}
